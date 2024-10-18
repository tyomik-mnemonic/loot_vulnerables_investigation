import requests
from logger.logger import logger

default = {
    "q": "language:python",  # Поиск репозиториев с языком Python
    "sort": "stars",  # Сортировка по количеству звезд
    "order": "desc",  # По убыванию
    "per_page": 10  # Количество результатов на странице
}

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
            response = self.session.get(self.api_url, params=self.params)
            response.raise_for_status()
            return response.json()
        except Exception as ex:
            logger.warning(ex)