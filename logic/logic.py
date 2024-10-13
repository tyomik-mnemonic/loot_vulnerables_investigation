from typing import Dict, Any
class Logic:
    
    @classmethod
    async def result_processing(data:Dict[Any, Any]):
        reposes = []
        for repo in data["items"]:
            reposes.append(
                {
                    "name": repo['name'],
                    "stars": repo['stargazers_count'],
                    "forks_stars": repo['forks_count']
                }
            )
        pass
