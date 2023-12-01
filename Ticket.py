from datetime import datetime


class Ticket:
    def __init__(self, owner, projection, seat_label, status):
        self.owner = owner
        self.projection = projection
        self.seat_label = seat_label
        self.date = datetime.now()
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def update_owner(self, new_owner):
        self.owner = new_owner

    def update_seat_label(self, new_seat_label):
        self.seat_label = new_seat_label
