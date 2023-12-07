from CinemaHall import CinemaHall


def save_cinema_hall(cinema_hall):
    with open('cinemahalls.txt', 'a') as file:
        file.write(f"{cinema_hall.hall_code}|{cinema_hall.num_rows}|{cinema_hall.seat_labels}|{cinema_hall.hall_name}")


class CinemaHallController:
    def __init__(self):
        self.list_of_cinema_halls = []

    def load_cinema_halls(self):
        with open('cinemahalls.txt', 'r') as file:
            for line in file:
                new_cinema_hall = line.strip().split('|')
                self.list_of_cinema_halls.append(CinemaHall(*new_cinema_hall))
