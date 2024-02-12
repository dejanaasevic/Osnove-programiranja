from datetime import datetime


class MovieProjectionTermCriterion:
    def __init__(self, title=None, hall_code=None, date=None, start_time=None, end_time=None):
        self.title = title
        self.hall_code = hall_code
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def valid_projection_term(self, projection_term):
        if (self.title is not None and self.title.lower().strip() not in
                projection_term.movie_projection.movie.lower().strip()):
            return False
        if self.hall_code is not None and self.hall_code != projection_term.movie_projection.hall.hall_code:
            return False

        if self.date is not None:
            date_object = datetime.strptime(self.date, '%d.%m.%Y.')
            if date_object != projection_term.date:
                return False
        if self.start_time is not None and self.start_time != projection_term.movie_projection.start_time.strftime("%H:%M"):
            return False

        if self.end_time is not None and self.end_time != projection_term.movie_projection.end_time.strftime("%H:%M"):
            return False

        return True
