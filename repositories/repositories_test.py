import os
import tempfile
import unittest
from repositories.repositories import DataProcessor
import pytest

class TestDataProcessor(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
    
def __init(self):
    pass
def test_save_to_csv_with_special_characters(self):
    test_data = [
        {"name": "repo/with/slashes", "stars": 100, "forks_stars": 50},
        {"name": "repo\"with\"quotes", "stars": 200, "forks_stars": 75},
        {"name": "repo,with,commas", "stars": 300, "forks_stars": 100}
    ]
    processor = DataProcessor(db_config="dummy_config")
    processor.data = test_data

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_file:
        temp_file_path = temp_file.name
        processor.save_to_csv(temp_file_path)

    with open(temp_file_path, 'r') as file:
        csv_content = file.read()

    expected_content = (
        "name,stars,forks_stars\n"
        "repo/with/slashes,100,50\n"
        "\"repo\"\"with\"\"quotes\",200,75\n"
        "\"repo,with,commas\",300,100\n"
    )
    self.assertEqual(csv_content, expected_content)

    os.unlink(temp_file_path)

def test_create_dataframe_empty_data(self):
        processor = DataProcessor(db_config="dummy_config")
        processor.data = []
        df = processor.create_dataframe()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)
        self.assertEqual(list(df.columns), [])