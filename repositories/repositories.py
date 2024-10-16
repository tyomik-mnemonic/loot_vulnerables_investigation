import pandas as pd
from logic.logic import Logic
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import csv
import json

class DataProcessor:
    def __init__(self, db_config=None):
        self.db_config = db_config
    
    def create_dataframe(self):
        return pd.DataFrame(Logic.reposes)
    
    def save_to_database(self):
        if not self.db_config:
            raise ValueError("Database configuration is not provided.")
        
        engine = create_engine(self.db_config)
        
        with engine.connect() as conn:
            query = text("""
                INSERT INTO repositories (name, stars, forks_stars)
                VALUES (:name, :stars, :forks_stars)
            """)
            
            for repo in Logic.reposes:
                conn.execute(query, **repo)
    
    def save_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['name', 'stars', 'forks_stars']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(Logic.reposes)
    
    def save_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(Logic.reposes, file, indent=4)