from MovieProjection import MovieProjection
from CinemaHallController import CinemaHallController


# radila u verziji gde je parametar hall predstavljao oznaku a ne objekat
def save_projection(movie_projection):
    with open('projections.txt', 'a') as file:
        projection_info = (f"{movie_projection.projection_code}|{movie_projection.hall.hall_code}"
                           f"|{movie_projection.start_time}"f"|{movie_projection.end_time}|"
                           f"{movie_projection.projection_days}|{movie_projection.movie}|"
                           f"{movie_projection.ticket_price}\n")
        file.write(projection_info)


cinema_controller = CinemaHallController()
cinema_controller.load_cinema_halls()
list_of_halls = cinema_controller.list_of_cinema_halls


class MovieProjectionController:
    def __init__(self):
        self.list_of_projections = []

    def load_projections(self):
        with open('projections.txt', 'r') as file:
            for line in file:
                new_projection = line.strip().split('|')
                for hall in list_of_halls:
                    if hall.hall_code == new_projection[1]:
                        self.list_of_projections.append(MovieProjection(new_projection[0], hall, new_projection[2],
                                                                        new_projection[3], new_projection[4],
                                                                        new_projection[5], new_projection[6]))

    def add_projection(self, projection):
        if isinstance(projection, MovieProjection):
            self.list_of_projections.append(projection)
            save_projection(projection)
            return True
        else:
            if not isinstance(projection, MovieProjection):
                print("Prosleđen objekat nije tipa MovieProjection")
                return False
