from MovieProjection import MovieProjection


# radila u verziji gde je parametar hall predstavljao oznaku a ne objekat
def save_projection(movie_projection):
    with open('projections.txt', 'a') as file:
        projection_info = (f"{movie_projection.projection_code}|{movie_projection.hall}"
                           f"|{movie_projection.start_time}"f"|{movie_projection.end_time}|"
                           f"{movie_projection.projection_days}|{movie_projection.movie}|"
                           f"{movie_projection.ticket_price}\n")
        file.write(projection_info)


class MovieProjectionController:
    def __init__(self):
        self.list_of_projections = []

    def load_projections(self):
        with open('projections.txt', 'r') as file:
            for line in file:
                new_projection = line.strip().split('|')
                self.list_of_projections.append(MovieProjection(*new_projection))
