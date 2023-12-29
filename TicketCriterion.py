from datetime import datetime, date


class TicketCriterion:
    def __init__(self, code=None, owner=None, date=None, start_time=None, end_time=None, status=None):
        self.code = code
        self.owner = owner
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def valid_ticket(self, ticket):
        if self.code is not None and self.code != ticket.projection_term.code[:4]:
            return False
        if self.date is not None:
            ticket_date_string = ticket.date.strftime('%d.%m.%Y.')
            if ticket_date_string != self.date:
                return False
        if self.start_time is not None and self.start_time != ticket.projection_term.movie_projection.start_time:
            return False
        if self.end_time is not None and self.end_time != ticket.projection_term.movie_projection.end_time:
            return False
        if self.status is not None and int(self.status) != int(ticket.status):
            return False
        if self.owner is not None:
            owner = self.owner.split()
            for owner_item in owner:
                if owner_item not in ticket.owner:
                    return False
        return True
