from DisplayController import DisplayController
from TicketController import TicketController


class ReportController:
    def sold_tickets_by_sale_date(self, date_choice):
        ticket_controller = TicketController()
        ticket_controller.load_tickets()
        list_of_tickets = ticket_controller.list_of_tickets
        display_controller = DisplayController()
        filtered_tickets = []
        for ticket in list_of_tickets:
            string_date = ticket.date.strftime("%d.%m.%Y.")
            if string_date == date_choice and ticket.status == "2":
                filtered_tickets.append(ticket)
        if not filtered_tickets:
            print("Nema pronađenih karata. Molimo pokušajte ponovo.")
        else:
            table = display_controller.display_sold_tickets_by_sale_date(filtered_tickets)
            print(f"Lista prodatih karata za odabran datum prodaje: {date_choice}")
            print()
            print(table)
            with open('report_sold_tickets_by_sale_date.txt', 'a', encoding='utf-8') as file:
                file.write(f"Lista prodatih karata za odabran datum prodaje: {date_choice}\n")
                file.write(table + "\n")

