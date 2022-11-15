from flask_restful import Resource
class Movie(Resource):
    def __init__(self, movieID, title, genres):
        self.movieID = movieID
        self.title = title
        self.genres = genres
