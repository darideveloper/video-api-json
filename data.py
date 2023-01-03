import os
import json
import datetime

# Global variables
JSON_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

def query_films ():
    """ Get films from JSON file

    Returns:
        list: list of dictionaries with films data
    """
    with open(JSON_PATH, 'r', encoding='UTF-8') as file:
        json_data = json.loads(file.read())
        return json_data["films"]
    
def query_film (id):
    """ Get simgle film from JSON file

    Returns:
        dict: film data
    """
    with open(JSON_PATH, 'r', encoding='UTF-8') as file:
        json_data = json.loads(file.read())
        if json_data["films"][id]:
            return json_data["films"][id]
        else: 
            ""
    
def save_films (new_films):
    """ Update films in JSON file
    """
    
    # Get original data
    with open(JSON_PATH, 'r', encoding='UTF-8') as file:
        json_data = json.loads(file.read())
    
    # Get current date and replace it
    date = datetime.datetime.now ().strftime("%Y/%m/%d")
    json_data["last_update"] = date
    
    # Replace films and save
    json_data["films"] = new_films
    with open(JSON_PATH, 'w', encoding='UTF-8') as file:
        file.write(json.dumps(json_data))