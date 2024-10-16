from typing import Dict, Any, Never
class Logic:
    reposes = []
    @classmethod
    async def result_processing(cls:type, data_param:Dict[Any, Any])->Never:
        
        for repo in data_param["items"]:
            cls.reposes.append(
                {
                    "name": repo['name'],
                    "stars": repo['stargazers_count'],
                    "forks_stars": repo['forks_count']
                }
            )
        return None
