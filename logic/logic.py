from typing import Dict, Any, Never
from web.requester import Requester

class Logic:
    """
    Класс для обработки данных о репозиториях.

    Этот класс предоставляет функциональность для обработки и храненияpass
    информации о репозиториях, полученной из внешнего источника.

    Атрибуты:
        reposes (list): Список словарей, содержащих информацию о репозиториях.
            Каждый словарь содержит ключи 'name', 'stars' и 'forks_stars'.

    Методы:
        result_processing(cls, data_param): Асинхронный метод класса для обработки
            входных данных и заполнения списка reposes.

    Примечание:
        Этот класс использует аннотации типов из модуля typing.
    """
    
    reposes = []
    @classmethod
    def result_processing(
        cls:type,
        data_param:Dict[Any, Any]=None
    )->Never:
        
        requester = Requester()
        data_param = requester.request_result
        
        for repo in data_param["items"]:
            cls.reposes.append(
                {
                    "name": repo['name'],
                    "stars": repo['stargazers_count'],
                    "forks_stars": repo['forks_count']
                }
            )
        return None
