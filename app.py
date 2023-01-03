from flask import Flask, request
from flask_cors import CORS
from data import query_films, query_film, save_films

# Start app
app = Flask(__name__)
CORS(app)
        
@app.get('/<int:id>/')
def get_film (id):
    """ Get data from single film, using the position in the films list

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
        return {"error": "Film not found"}, 404
    
@app.get('/all/')
def get_all_film ():
    """ Get data from all films with pagination

    Returns:
        dicctionary: data of all films 
    """

    # Get pagination data 
    page = request.args.get('page', '')
    results_per_page = request.args.get('results-per-page', '')
    
    # Return error if pagination data is not valid
    if not page or not results_per_page:
        return {"error": "'page' and 'results-per-page' are required in the url (as get parameters)"}, 400
        
    # Get films using pagination        
    films = query_films()
    start = (int(page) - 1) * int(results_per_page)
    end = start + int(results_per_page)
    films_pagination = films[start:end]
    
    # Check if there are more results
    more_results = False
    if len(films) >= end:
        more_results = True
    
    return {
        "films": films_pagination,
        "total_films": len(films),
        "current_page": page,
        "results_per_page": results_per_page,
        "more_results": more_results
    }, 200
    
    
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
    """ Updata data from single film, using the position in the films list
    
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
        return {"error": "Film not found"}, 404
    
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
        return {"error": "Film not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)