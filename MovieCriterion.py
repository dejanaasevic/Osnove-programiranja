class MovieCriterion:
    def __init__(self, title=None, genre=None, duration=None, director=None, main_roles=None,
                 country_of_origin=None, release_year=None, description=None,
                 min_duration=None, max_duration=None):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.director = director
        self.main_roles = main_roles
        self.country_of_origin = country_of_origin
        self.release_year = release_year
        self.description = description
        self.min_duration = min_duration
        self.max_duration = max_duration

    def valid_movie(self, movie):
        if self.title is not None and self.title.lower() not in movie.title.lower().strip():
            return False
        if self.genre is not None and self.genre.lower() not in movie.genre.lower().strip():
            return False
        if self.duration is not None and int(self.duration) != int(movie.duration):
            return False
        if self.director is not None and self.director.lower() not in movie.director.lower().strip():
            return False
        if self.main_roles is not None and self.main_roles.lower() not in movie.main_roles.lower().strip():
            return False
        if (self.country_of_origin is not None and self.country_of_origin.lower()
                not in movie.country_of_origin.lower().strip()):
            return False
        if self.release_year is not None and self.release_year != movie.release_year:
            return False
        if self.description is not None and self.description.lower() not in movie.description.lower().strip():
            return False
        if self.min_duration is not None and int(movie.duration) <= int(self.min_duration):
            return False
        if self.max_duration is not None and int(movie.duration) >= int(self.max_duration):
            return False

        return True

