import pandas as pd
from logic.logic import Logic
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import csv
import json

protodata = Logic.result_processing()
protodata = Logic.reposes

class DataProcessor:
    """
    Класс для обработки и сохранения данных о репозиториях.

    Этот класс предоставляет методы для работы с данными репозиториев,
    включая создание DataFrame, сохранение в базу данных, CSV и JSON файлы.

    Атрибуты:
        db_config (str): Строка конфигурации для подключения к базе данных.

    Методы:
        create_dataframe(): Создает DataFrame из данных репозиториев.
        save_to_database(): Сохраняет данные репозиториев в базу данных.
        save_to_csv(file_path): Сохраняет данные репозиториев в CSV файл.
        save_to_json(file_path): Сохраняет данные репозиториев в JSON файл.
    """
    def __init__(self, db_config=None):
        self.db_config = db_config
        self.data = protodata
        return
    
    def create_dataframe(self):
        return pd.DataFrame(self.data)
    
    def save_to_database(self):
        if not self.db_config:
            raise ValueError("Database configuration is not provided.")
        
        engine = create_engine(self.db_config)
        
        with engine.connect() as conn:
            query = text("""
                INSERT INTO repositories (name, stars, forks_stars)
                VALUES (:name, :stars, :forks_stars)
            """)
            
            for repo in self.data:
                conn.execute(query, **repo)
    
    def save_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['name', 'stars', 'forks_stars']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(self.data)
    
    def save_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.data, file, indent=4)