from datetime import datetime, timedelta


class MovieProjection:
    def __init__(self, projection_code, hall, start_time, end_time, projection_days, movie, ticket_price):
        self.projection_code = projection_code
        self.hall = hall
        self.start_time = start_time
        self.end_time = end_time
        self.projection_days = projection_days
        self.movie = movie
        self.ticket_price = ticket_price

    @staticmethod
    def calculate_new_ending(time, duration):
        if str(type(time)) == "<class 'datetime.time'>":
            start_time = time.strftime("%H:%M")
        else:
            start_time = time
        start_time = datetime.strptime(start_time, "%H:%M")
        end_time = start_time + timedelta(minutes=int(duration))
        if end_time.hour >= 24:
            end_time = end_time.replace(hour=end_time.hour - 24)
        elif end_time.hour < 0:
            end_time = end_time.replace(hour=end_time.hour + 24)

        minutes = end_time.minute
        if minutes > 30:
            end_time = end_time.replace(minute=0, hour=end_time.hour + 1)
        elif minutes < 30 and minutes != 0:
            end_time = end_time.replace(minute=30)
        return end_time.strftime("%H:%M")
