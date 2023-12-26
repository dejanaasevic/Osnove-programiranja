import re
from tabulate import tabulate


class CinemaHall:
    def __init__(self, hall_code, num_rows, seat_labels, hall_name=None):
        self.hall_code = hall_code
        self.hall_name = hall_name
        self.num_rows = int(num_rows)
        self.seat_labels = seat_labels
        self.seat_labels_array = seat_labels.strip().split(',')
        self.seating_plan = self.generate_seating_plan()

    def generate_seating_plan(self):
        rows = {}
        for row_number in range(1, self.num_rows + 1):
            row_label = str(row_number)
            seats = {}
            for seat_label in self.seat_labels_array:
                seats[seat_label] = False
            rows[row_label] = seats
        return rows

    def get_total_seats(self):
        return self.num_rows * len(self.seat_labels_array)

    def get_available_seats(self):
        available_seats = []
        for row_number in self.seating_plan:
            for seat_label in self.seat_labels_array:
                if not self.seating_plan[row_number][seat_label]:
                    available_seats.append("Row: " + row_number + " , Seat: " + seat_label)
        return available_seats

    def reserve_seat1(self, row, seat):
        if row in self.seating_plan and seat in self.seating_plan[row]:
            if not self.seating_plan[row][seat]:
                self.seating_plan[row][seat] = True
                return True
        return False

    def reserve_seat(self, row, seat):
        if row in self.seating_plan and seat in self.seating_plan[row]:
            if not self.seating_plan[row][seat]:
                self.seating_plan[row][seat] = True
                return True
            else:
                print("Sediste je vec zauzeto.")
                return False
        else:
            print("Neispravno oznaceno sediste ili red.")
        return False

    def display_seating_plan(self):
        for row_number in self.seating_plan:
            row_display = "Row " + row_number + ": "
            for seat_label in self.seat_labels_array:
                if self.seating_plan[row_number][seat_label]:
                    row_display += "X "
                else:
                    row_display += seat_label + " "
            print(row_display.strip())

    def display_cinema_hall(self):
        hall_data = [
            ["Hall Code", self.hall_code],
            ["Hall Name", self.hall_name if self.hall_name else ""],
            ["Number of Rows", self.num_rows],
            ["Seat Labels", ", ".join(self.seat_labels)]
        ]

        table = tabulate(hall_data, headers=["Attribute", "Information"], tablefmt="grid")
        print(table)

    @staticmethod
    def valid_hall_code(hall_code):
        return len(hall_code) == 1 and hall_code.isalpha() and hall_code.isupper()

    @staticmethod
    def valid_seat_label(seat_label):
        pattern = r'^\d+[A-Z]$'
        return bool(re.match(pattern, seat_label))

    @staticmethod
    def valid_seat_labels(seat_labels):
        pattern = r"^[A-Z](,[A-Z])*$"
        return bool(re.match(pattern, seat_labels))

    @staticmethod
    def valid_cinema_hall_name(cinema_hall_name):
        pattern = r"^[A-Z][a-zA-Z0-9\s]*$"
        return bool(re.match(pattern, cinema_hall_name))

    @staticmethod
    def valid_num_rows(num_rows):
        pattern = r"^[1-9]\d*$"
        return bool(re.match(pattern, num_rows))
