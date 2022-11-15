import csv
import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Movie(Resource):
    def __init__(self, movieID, title, genres):
        self.movieID = movieID
        self.title = title
        self.genres = genres


@app.route('/movies', methods=['GET'])
def movie_page():
    movie_list = []

    with open('test.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip header
        for movieID, title, genres in reader:
            movie_list.append(Movie(movieID, title, genres))

    data_set = json.dumps([ob.__dict__ for ob in movie_list], indent=5)

    return data_set

if __name__ == '__main__':
    app.run(debug=True)