#from web.requester import Requester
from repositories.repositories import DataProcessor

def main():
    x = DataProcessor()
    df = x.create_dataframe()
    df.to_csv('repositories-two.csv', index=False)
    csv = x.save_to_csv('repositories.csv')
    
   
main()