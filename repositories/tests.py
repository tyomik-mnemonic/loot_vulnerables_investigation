import unittest
import os
from repositories.repositories import DataProcessor, Logic

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        Logic.reposes = [
            {"name": "repo1", "stars": 100, "forks_stars": 50},
            {"name": "repo2", "stars": 200, "forks_stars": 75},
            {"name": "repo3", "stars": 150, "forks_stars": 60}
        ]
        
        self.processor = DataProcessor()
    
    def test_create_dataframe(self):
        df = self.processor.create_dataframe()
        self.assertEqual(len(df), 3)
        self.assertEqual(list(df.columns), ["name", "stars", "forks_stars"])
    
    def test_save_to_csv(self):
        file_path = "test_repositories.csv"
        self.processor.save_to_csv(file_path)
        
        with open(file_path, "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 4)  # 3 строки данных + заголовок
        
        os.remove(file_path)
    
    def test_save_to_json(self):
        file_path = "test_repositories.json"
        self.processor.save_to_json(file_path)
        
        with open(file_path, "r") as file:
            data = json.load(file)
            self.assertEqual(len(data), 3)
        
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()