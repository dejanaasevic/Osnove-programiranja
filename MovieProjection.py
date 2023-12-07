class MovieProjection:
    def __init__(self, projection_code, hall, start_time, end_time, projection_days, movie, ticket_price):
        self.projection_code = projection_code
        self.hall = hall
        self.start_time = start_time
        self.end_time = end_time
        self.projection_days = projection_days
        self.movie = movie
        self.ticket_price = ticket_price

    def display_movie_projection(self):
        print(f"Projection Code: {self.projection_code}\nHall: {self.hall}\nStart Time: {self.start_time}\n"
              f"End Time: {self.end_time}\nProjection Days: {self.projection_days}\nMovie: {self.movie}\n"
              f"Ticket Price: {self.ticket_price}")
