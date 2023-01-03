import os
import json
from flask import Flask, request
from flask_cors import CORS

# Start app
app = Flask(__name__)
CORS(app)

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
    film = query_film(id)
    
    if film:
        # Return fil data if exist
        return film, 200
    else: 
        # Return error if film not exist
        return {"error": "Film not found"}, 400  
    
@app.post('/')
def post_film ():
    """ Save new film in JSON file

    Returns:
        dicctionary: confirmation or error message
    """
    
    # Get all films
    films = query_films()
    
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

@app.put ('/<int:id>/')
def put_film (id):
    """ Updata data from simgle film, using the position in the films list
    
    Returns:
        dicctionary: confirmation or error message
    """
    
    # Get all films
    films = query_films()
    
    # Get new film data from json
    new_data = request.get_json()
    
    # Get current film data
    film = query_film(id)
    
    if film:
        # Update data if film exist
        for key, value in new_data.items():
            film[key] = value
        films[id] = film
        save_films (films)
        return {"message": "Film updated"}, 200
    else: 
        # Return error if film not exist
        return {"error": "Film not found"}, 400  
    
@app.delete ('/<int:id>/')
def delete_film (id):
    """ Delete a film, using the position in the films list
    
    Returns:
        dicctionary: confirmation or error message
    """
    
    # Get all films
    films = query_films()   
    
    if len(films) > id:
        # Update data if film exist
        del films[id]
        save_films (films)
        return {"message": "Film deleted. IDs updated"}, 200
    else: 
        # Return error if film not exist
        return {"error": "Film not found"}, 400  

if __name__ == '__main__':
    app.run(debug=True)