import os
import json
from flask import Flask
from flask_cors import CORS

# Start app
app = Flask(__name__)
CORS(app)

# Global variables
JSON_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

def get_films ():
    """ Get films from JSON file

    Returns:
        list: list of dictionaries with films data
    """
    with open(JSON_PATH, 'r', encoding='UTF-8') as file:
        json_data = json.loads(file.read())
        return json_data["films"]
        
@app.get('/<int:id>/')
def index (id):
    """ Get data from simgle film, using the position in the films list

    Args:
        id (int): position of the film

    Returns:
        dicctionary: data of the film or error message
    """
    films = get_films()
    if films[id]:
        return films[id]
    else: 
        return {"error": "Film not found"}, 400        
    

if __name__ == '__main__':
    app.run(debug=True)