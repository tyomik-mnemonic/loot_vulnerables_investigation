import requests
from logger.logger import logger
import yaml


default = {
    "q": "language:python",  # Поиск репозиториев с языком Python
    "sort": "stars",  # Сортировка по количеству звезд
    "order": "desc",  # По убыванию
    "per_page": 10  # Количество результатов на странице
}

#Загрузка конфигурации
config = open('configs.yaml', 'r')
config = yaml.safe_load(config)

creds = open('.configs.yaml', 'r')
creds = yaml.safe_load(creds)


class Requester(object):
    """
    Класс для запроса данных с GitHub API.

    Атрибуты:
        api_url (str): URL для API GitHub.
        params (dict): Параметры для запроса.
        session (requests.Session): Сессия для запросов.
    """
    def __init__(
        self, 
        api_url:str="https://api.github.com/search/repositories",
        params:dict=default
    ):
        self.api_url = api_url
        self.params = params
        self.session = requests.Session()
        self.request_result = self.run_pipe()
        
    def run_pipe(self):
        return self.get_data()
    
    def get_data(self):
        try:
            #чекам проход по объектам из конфиг тут (по подгруппам репозиториев)
            #response = self.session.get(self.api_url, params=self.params) if self.params == default else [
            #    self.session.get(self.api_url, params=i) for i in self.params
            #]
            response = []
        
            #для каждого пайпа добавляю авторизацию
            if self.params != default:
                for i in self.params:
                    h = {}
                    h['Authorization'] = creds['creds']['token']
                    h['Accept'] = 'application/vnd.github.v3+json'
                    r = self.session.get(self.api_url, params=i, headers=h)
                    r.raise_for_status()
                    response.append(r)
            else:
                response = self.session.get(self.api_url, params=default)
                response.raise_for_status()
                
            
            return response.json() if  self.params == default else [r.json() for r in response]
        except Exception as ex:
            logger.warning(ex)