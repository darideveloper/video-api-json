from flask import Flask, request
from flask_cors import CORS
from data import query_films, query_film, save_films

# Start app
app = Flask(__name__)
CORS(app)
        
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