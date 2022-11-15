from flask_restful import Resource


class Link(Resource):
    def __init__(self, movieID, imdbId, tmdbId):
        self.movieID = movieID
        self.imdbId = imdbId
        self.tmdbId = tmdbId
