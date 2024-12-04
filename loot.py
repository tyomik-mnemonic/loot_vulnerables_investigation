import requests
import yaml
import random

# Укажите свой GitHub токен здесь
GITHUB_TOKEN = 'your_github_token_here'

# Загрузка конфигурации

config = open('configs.yaml', 'r')
config = yaml.safe_load(config)

creds = open('.configs.yaml', 'r')
creds = yaml.safe_load(creds)

# Заголовки для авторизации
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

def search_repositories(criteria):
    repositories = []
    query_parts = []

    # Формирование поискового запроса
    if criteria.get('languages'):
        for language in criteria['languages']:
            query_parts.append(f'language:{language}')
    
    if criteria.get('star_ranges'):
        for star_range in criteria['star_ranges']:
            query_parts.append(f'stars:{star_range}')
    
    if criteria.get('topics'):
        for topic in criteria['topics']:
            query_parts.append(f'topic:{topic}')

    query = ' '.join(query_parts)
    print(f"Query: {query}")

    url = 'https://api.github.com/search/repositories'
    params = {
        'q': query,
        'sort': 'stars',
        'order': 'desc',
        'per_page': 100,
        'page': 1
    }

    while len(repositories) < criteria['count']:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Ошибка: {response.status_code}")
            break
        
        data = response.json()
        repositories.extend(data['items'])

        if 'next' not in response.links:
            break
        params['page'] += 1

    # Рандомный выбор нужного количества
    selected_repos = random.sample(repositories, min(criteria['count'], len(repositories)))
    
    return selected_repos

def main():
    for criterion in config['search_criteria']:
        print(f"Processing criterion: {criterion['name']}")
        repos = search_repositories(criterion)
        
        # Вывод информации о собранных репозиториях
        for repo in repos:
            print(f"Name: {repo['name']}, Stars: {repo['stargazers_count']}, URL: {repo['html_url']}")
        print(f"Total repositories selected for {criterion['name']}: {len(repos)}")

if __name__ == "__main__":
    main()
