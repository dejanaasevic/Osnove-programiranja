
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
                    available_seats.append("Red: " + row_number + " , Sedište: " + seat_label)
        return available_seats

    def reserve_seat(self, row, seat):
        if row in self.seating_plan and seat in self.seating_plan[row]:
            if not self.seating_plan[row][seat]:
                self.seating_plan[row][seat] = True
                return True
            else:
                print("Sedište je već zauzeto.")
                return False
        else:
            print("Neispravno označeno sedište ili red.")
        return False

    def display_seating_plan(self):
        for row_number in self.seating_plan:
            row_display = "Red " + row_number + ": "
            for seat_label in self.seat_labels_array:
                if self.seating_plan[row_number][seat_label]:
                    row_display += "X "
                else:
                    row_display += seat_label + " "
            print(row_display.strip())

