from CinemaHall import CinemaHall


def save_cinema_hall(cinema_hall):
    with open('cinemahalls.txt', 'a') as file:
        file.write(
            f"{cinema_hall.hall_code}|{cinema_hall.num_rows}|{cinema_hall.seat_labels}|{cinema_hall.hall_name}\n")


class CinemaHallController:
    def __init__(self):
        self.list_of_cinema_halls = []

    def load_cinema_halls(self):
        with open('cinemahalls.txt', 'r') as file:
            for line in file:
                new_cinema_hall = line.strip().split('|')
                self.list_of_cinema_halls.append(CinemaHall(*new_cinema_hall))

    def add_hall(self, cinemahall):
        if isinstance(cinemahall, CinemaHall):
            self.list_of_cinema_halls.append(cinemahall)
            save_cinema_hall(cinemahall)
            return True
        else:
            if not isinstance(cinemahall, CinemaHall):
                print("Prosleđen objekat nije tipa CinemaHall.")
                return False
