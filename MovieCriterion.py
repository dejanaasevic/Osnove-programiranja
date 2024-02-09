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
        if self.duration is not None and int(self.duration) != int(movie.duration):
            return False
        if self.country_of_origin is not None and self.country_of_origin.lower() not in movie.country_of_origin.lower().strip():
            return False
        if self.release_year is not None and self.release_year != movie.release_year:
            return False
        if self.description is not None and self.description.lower() not in movie.description.lower().strip():
            return False
        if self.min_duration is not None and int(movie.duration) <= int(self.min_duration):
            return False
        if self.max_duration is not None and int(movie.duration) >= int(self.max_duration):
            return False

        if self.main_roles is not None:
            actors = [actor.strip().lower() for actor in self.main_roles.split(',')]
            movie_actors = [m_actor.strip().lower() for m_actor in movie.main_roles.split(',')]
            for actor in actors:
                found = any(actor in m_actor for m_actor in movie_actors)
                if not found:
                    return False

        if self.director is not None:
            directors = [director.strip().lower() for director in self.director.split(',')]
            movie_directors = [m_director.strip().lower() for m_director in movie.director.split(',')]
            for director in directors:
                found = any(director in m_director for m_director in movie_directors)
                if not found:
                    return False

        if self.genre is not None:
            genres = [genre.strip().lower() for genre in self.genre.split()]
            movie_genre = [m_genre.strip().lower() for m_genre in movie.genre.split()]
            found = all(genre in movie_genre for genre in genres)
            if not found:
                return False

        return True
