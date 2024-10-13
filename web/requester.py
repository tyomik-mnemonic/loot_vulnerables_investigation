import requests
from logger.logger import logger

default = {
    "q": "language:python",  # Поиск репозиториев с языком Python
    "sort": "stars",  # Сортировка по количеству звезд
    "order": "desc",  # По убыванию
    "per_page": 10  # Количество результатов на странице
}

class Requester(object):
    async def __init__(self, api_url:str, params:dict):
        self.api_url = api_url
        self.params = params
        self.session = requests.Session()
        
        
    async def run_pipe(self):
        pass
    
    async def get_data(self):
        try:
            response = await self.session.get(self.api_url, params=self.params)
            response.raise_for_status()
            return response.json()
        except Exception as ex:
            logger.warning(ex)