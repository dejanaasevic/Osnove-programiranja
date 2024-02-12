from datetime import datetime
from MovieProjection import MovieProjection
from CinemaHallController import CinemaHallController


def save_projection(movie_projection):
    with open('projections.txt', 'a', encoding='utf-8') as file:
        projection_info = (f"{movie_projection.projection_code}|{movie_projection.hall.hall_code}"
                           f"|{movie_projection.start_time}"f"|{movie_projection.end_time}|"
                           f"{movie_projection.projection_days}|{movie_projection.movie}|"
                           f"{movie_projection.ticket_price}\n")
        file.write(projection_info)


cinema_controller = CinemaHallController()
cinema_controller.load_cinema_halls()
list_of_halls = cinema_controller.list_of_cinema_halls


def remove_projection_from_file(projection):
    with open('projections.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('projections.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            projection_info = line.strip().split('|')
            if (projection_info[0] == projection.projection_code and projection_info[1] == projection.hall.hall_code
                    and projection_info[2] == projection.start_time.strftime("%H:%M") and
                    projection_info[3] == projection.end_time.strftime("%H:%M") and
                    projection_info[4] == projection.projection_days and projection_info[5] == projection.movie):
                print(f"obrisana projekcija: {projection.projection_code}")
                continue
            else:
                file.write(line)


def update_projection_in_file(file_projection, updated_projection):
    with open('projections.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('projections.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            data = line.strip().split('|')
            start_time = None
            end_time = None

            if str(type(file_projection.start_time)) == "<class 'datetime.time'>":
                start_time = file_projection.start_time.strftime("%H:%M")
            else:
                start_time = file_projection.start_time
            if str(type(file_projection.end_time)) == "<class 'datetime.time'>":
                end_time = file_projection.end_time.strftime("%H:%M")
            else:
                end_time = file_projection.end_time

            if (data[0] == file_projection.projection_code and
                    data[1] == file_projection.hall.hall_code and
                    data[2] == start_time and
                    data[3] == end_time and
                    data[4] == file_projection.projection_days and
                    data[5] == file_projection.movie):

                start_time = None
                end_time = None

                if str(type(updated_projection.start_time)) == "<class 'datetime.time'>":
                    start_time = updated_projection.start_time.strftime("%H:%M")
                else:
                    start_time = updated_projection.start_time
                if str(type(updated_projection.end_time)) == "<class 'datetime.time'>":
                    end_time = updated_projection.end_time.strftime("%H:%M")
                else:
                    end_time = updated_projection.end_time

                updated_line = "|".join([
                    updated_projection.projection_code,
                    updated_projection.hall.hall_code,
                    start_time,
                    end_time,
                    updated_projection.projection_days,
                    updated_projection.movie,
                    updated_projection.price
                ]) + "\n"
                file.write(updated_line)
            else:
                file.write(line)


class MovieProjectionController:
    def __init__(self):
        self.list_of_projections = []

    def load_projections(self):
        with open('projections.txt', 'r', encoding='utf-8') as file:
            for line in file:
                new_projection = line.strip().split('|')
                for hall in list_of_halls:
                    start_time = datetime.strptime(new_projection[2], "%H:%M").time()
                    end_time = datetime.strptime(new_projection[3], "%H:%M").time()
                    if hall.hall_code == new_projection[1]:
                        self.list_of_projections.append(MovieProjection(new_projection[0], hall, start_time,
                                                                        end_time, new_projection[4],
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

    def update_projection(self, file_projection, updated_projection):
        update_projection_in_file(file_projection, updated_projection)
        return True

    def remove_projections(self, delete_projection):
        if not delete_projection:
            return
        for projection in delete_projection:
            self.remove_projection(projection)

    def remove_projection(self, projection_choice):
        for projection in self.list_of_projections:
            if projection.movie == projection_choice.movie:
                remove_projection_from_file(projection)
                self.list_of_projections.remove(projection)
                return True
        return True
