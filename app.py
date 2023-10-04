from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        'id': 1,
        'titulo': 'Blue Beetle',
        'lead actor': 'Xolo Maridueña' 
    },
    {
        'id': 2,
        'titulo': 'Wonder Woman',
        'lead actor': 'Gal Gadot'
    },
    {
        'id': 3,
        'titulo': 'Black Panther',
        'lead actor': 'Chadwick Boseman'
    },
    {
        'id': 4,
        'titulo': 'Spider-Man',
        'lead actor': 'Tom Holland'
    }
]

@app.route('/movies',methods=['GET'])
def get_movie():
    return jsonify(movies)

@app.route('/movies/<int:id>',methods=['GET'])
def get_movie_by_id(id):
    for movie in movies:
        if movie.get('id') == id:
            return jsonify(movie)

@app.route('/movies/<int:id>',methods=['PUT'])
def edit_movie_by_id(id):
    edited_movie = request.get_json()
    for index, movie in enumerate(movies):
        if movie.get('id') == id:
            movies[index].update(edited_movie)
            return jsonify(movies[index])
        
@app.route('/movies',methods=['POST'])
def add_new_movie():
    new_movie = request.get_json()
    movies.append(new_movie)

    return jsonify(movies)

@app.route('/movies/<int:id>',methods=['DELETE'])
def del_movie(id):
    for index, movie in enumerate(movies):
        if movie.get('id') == id:
            del movies[index]

    return jsonify(movies)


app.run(port=5000,host='localhost',debug=True)