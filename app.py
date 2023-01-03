import os
import json
from flask import Flask, request
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
    
def save_films (new_films):
    """ Update films in JSON file
    """
    
    with open(JSON_PATH, 'r', encoding='UTF-8') as file:
        json_data = json.loads(file.read())
    
    json_data["films"] = new_films
    with open(JSON_PATH, 'w', encoding='UTF-8') as file:
        file.write(json.dumps(json_data))
        
@app.get('/<int:id>/')
def get_film (id):
    """ Get data from simgle film, using the position in the films list

    Args:
        id (int): position of the film

    Returns:
        dicctionary: data of the film or error message
    """
    films = get_films()
    
    if films[id]:
        # Return fil data if exist
        return films[id], 200
    else: 
        # Return error if film not exist
        return {"error": "Film not found"}, 400  
    
@app.post('/')
def post_film ():
    """ Save new film in JSON file

    Returns:
        dicctionary: confirmation or error message
    """
    
    films = get_films()
    
    # Get new film data from json
    new_film = request.get_json()
    
    if new_film in films:
        # return error if film already exists
        return {"error": "Film already exists"}, 400
    else:
        # Save fil data in json file
        films.append (new_film)
        save_films (films)        
        
        # return confirmation message
        return {"message": "Film added"}, 200

if __name__ == '__main__':
    app.run(debug=True)