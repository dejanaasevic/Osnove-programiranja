class CinemaHall:
    def __init__(self, hall_code, hall_name, num_rows, seat_labels):
        self.hall_code = hall_code
        self.hall_name = hall_name
        self.num_rows = num_rows
        self.seat_labels = seat_labels
        self.seating_plan = self.generate_seating_plan()

    def generate_seating_plan(self):
        rows = {}
        for row_number in range(1, self.num_rows + 1):
            row_label = str(row_number)
            seats = {}
            for seat_label in self.seat_labels:
                seats[seat_label] = False
                rows[row_label] = seats
        return rows

    def get_total_seats(self):
        return self.num_rows * len(self.seat_labels)

    def get_available_seats(self):
        available_seats = []
        for row_number in self.seating_plan:
            for seat_label in self.seat_labels:
                if not self.seating_plan[row_number][seat_label]:
                    available_seats.append("Row: " + row_number + " , Seat: " + seat_label)
        return available_seats

    def reserve_seat(self, row, seat):
        if row in self.seating_plan and seat in self.seating_plan[row]:
            if not self.seating_plan[row][seat]:
                self.seating_plan[row][seat] = True
                return True
        return False

