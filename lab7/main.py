import csv
import json
from flask import Flask
from flask_restful import Resource, Api
import Classes.Movie as MovieClass
import Classes.Link as LinkClass
import Classes.Rating as RatingClass
import Classes.Tag as TagClass

app = Flask(__name__)
api = Api(app)


@app.route('/movies', methods=['GET'])
def movie_page():
    movie_list = []

    with open('movies.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip header
        for movieID, title, genres in reader:
            movie_list.append(MovieClass.Movie(movieID, title, genres))

    data_set = json.dumps([ob.__dict__ for ob in movie_list], indent=5)

    return data_set


@app.route('/links', methods=['GET'])
def link_page():
    link_list = []

    with open('links.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip header
        for movieID, imdbId, tmdbId in reader:
            link_list.append(LinkClass.Link(movieID, imdbId, tmdbId))

    data_set = json.dumps([ob.__dict__ for ob in link_list], indent=5)

    return data_set


@app.route('/ratings', methods=['GET'])
def rating_page():
    rating_list = []

    with open('ratings.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip header
        for userId, movieId, rating, timestamp in reader:
            rating_list.append(RatingClass.Rating(userId,
                                                  movieId, rating, timestamp))

    data_set = json.dumps([ob.__dict__ for ob in rating_list], indent=5)

    return data_set


@app.route('/tags', methods=['GET'])
def tag_page():
    tag_list = []

    with open('tags.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip header
        for userId, movieId, tag, timestamp in reader:
            tag_list.append(TagClass.Tag(userId, movieId, tag, timestamp))

    data_set = json.dumps([ob.__dict__ for ob in tag_list], indent=5)

    return data_set


if __name__ == '__main__':
    app.run(debug=True)
