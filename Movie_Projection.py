from datetime import datetime
import random
import string


class ProjectionTerm:
    def __init__(self, movie_projection, date):
        self.movie_projection = movie_projection
        self.date = datetime.strptime(date, '%d.%m.%Y')

    def get_day_of_week(self, date):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_of_week = date.weekday()
        return days_of_week[day_of_week]

    def valid_date(self, date):
        day_of_week = self.get_day_of_week(self.date)
        for day in self.movie_projection.projection_days:
            if day == day_of_week:
                return True
        return False

    def generate_code(self):
        formatted_date = self.date.strftime('%d.%m.%Y.')
        movie_projection_code = str(self.movie_projection.projection_code)
        abcd = string.ascii_uppercase
        random_code = ''.join(random.sample(abcd, 2))
        return  movie_projection_code + random_code + '|' + formatted_date


class MovieProjection:
    def __init__(self, projection_code, hall, start_time, end_time, projection_days, movie, ticket_price):
        self.projection_term = None
        self.projection_code = projection_code
        self.hall = hall
        self.start_time = start_time
        self.end_time = end_time
        self.projection_days = projection_days
        self.movie = movie
        self.ticket_price = ticket_price

    def set_projection_term(self, date):
        self.projection_term = ProjectionTerm(self, date)
