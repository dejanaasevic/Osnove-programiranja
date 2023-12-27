import re
from datetime import datetime

from tabulate import tabulate


class Ticket:
    def __init__(self, owner, projection_term, seat_label, status, date=None):
        self.owner = owner
        self.projection_term = projection_term
        self.seat_label = seat_label
        self.status = status
        if date is not None:
            self.date = datetime.strptime(date, '%d.%m.%Y.')
        else:
            self.date = datetime.now()


    def update_status(self, new_status):
        self.status = new_status

    def update_owner(self, new_owner):
        self.owner = new_owner

    def update_seat_label(self, new_seat_label):
        self.seat_label = new_seat_label

    def display_ticket_info(self):
        formatted_date = self.date.strftime('%d.%m.%Y.')
        ticket_info = [
            ["Owner", self.owner],
            ["Projection Term", self.projection_term],
            ["Seat Label", self.seat_label],
            ["Date", formatted_date],
            ["Status", self.status]
        ]
        table = tabulate(ticket_info, headers=["Attribute", "Information"], tablefmt="grid")
        print(table)

    @staticmethod
    def valid_name(name):
        pattern = r'^[A-Z][a-zA-Z]*(?:[\s,]+[A-Z][a-zA-Z]*)*$'
        return bool(re.match(pattern, name))
