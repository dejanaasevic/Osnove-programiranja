from datetime import datetime, timedelta

from DisplayController import DisplayController
from SoldTicketController import SoldTicketController
from TicketController import TicketController
from UserController import UserController


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

    def sold_tickets_by_projection_term_date(self, date_choice):
        ticket_controller = TicketController()
        ticket_controller.load_tickets()
        list_of_tickets = ticket_controller.list_of_tickets
        display_controller = DisplayController()
        filtered_tickets = []
        for ticket in list_of_tickets:
            string_date = ticket.projection_term.date.strftime("%d.%m.%Y.")
            if string_date == date_choice and ticket.status == "2":
                filtered_tickets.append(ticket)
        if not filtered_tickets:
            print("Nema pronađenih karata. Molimo pokušajte ponovo.")
        else:
            table = display_controller.display_sold_tickets_by_projection_term_date(filtered_tickets)
            print(f" Lista prodatih karata za odabran datum termina bioskopske projekcije: {date_choice}\n")
            print()
            print(table)
            with open('report_sold_tickets_by_projection_term_date.txt', 'a', encoding='utf-8') as file:
                file.write(f" Lista prodatih karata za odabran datum termina bioskopske projekcije: {date_choice}\n")
                file.write(table + "\n")

    def sold_tickets_by_date_and_sellperson(self, date_choice, sellperson_choice):
        sold_tickets_controller = SoldTicketController()
        sold_tickets_controller.load_sold_tickets()
        list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets
        display_controller = DisplayController()
        filtered_tickets = []
        for sold_ticket in list_of_sold_tickets:
            string_date = sold_ticket.ticket.date.strftime("%d.%m.%Y.")
            if string_date == date_choice and sold_ticket.sellperson == sellperson_choice:
                filtered_tickets.append(sold_ticket)
        if not filtered_tickets:
            print("Nema pronađenih karata. Molimo pokušajte ponovo.")
        else:
            table = display_controller.display_sold_tickets_by_date_and_sellperson(filtered_tickets)
            print("Lista prodatih karata za odabran datum prodaje i odabranog prodavca")
            print(f"datum: {date_choice}     prodavac: {sellperson_choice}\n")
            print(table)
            with open('report_sold_tickets_by_date_and_sellperson.txt', 'a', encoding='utf-8') as file:
                file.write(f"Lista prodatih karata za odabran datum prodaje i odabranog prodavca")
                file.write(f"datum:{date_choice}     prodavac:{sellperson_choice}\n")
                file.write(table + "\n")

    def sold_tickets_by_sale_day(self, day_choice):
        sold_tickets_controller = SoldTicketController()
        sold_tickets_controller.load_sold_tickets()
        list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets
        display_controller = DisplayController()
        date_choice = find_previous_date_by_day(int(day_choice))
        print(day_choice)
        filtered_tickets = []
        for sold_ticket in list_of_sold_tickets:
            string_date = sold_ticket.ticket.date.strftime("%d.%m.%Y.")
            if string_date == date_choice:
                filtered_tickets.append(sold_ticket)
        if not filtered_tickets:
            print("Nema pronađenih karata. Molimo pokušajte ponovo.")
        else:
            days = ['ponedeljak', 'utorak', 'sreda', 'četvrtak', 'petak', 'subota', 'nedelja']
            day = days[int(day_choice) - 1]
            table = display_controller.display_sold_tickets_by_sale_day(filtered_tickets)
            total_quantity = len(filtered_tickets)
            total_price = 0.0
            for sold_ticket in filtered_tickets:
                total_price += float(sold_ticket.price)

            print("Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) prodaje.\n")
            print(f"dan:{day}       datum:{date_choice}\n")
            print(table)
            print(f"ukupan broj prodatih karata: {total_quantity}   ukupna cena prodatih karata:{total_price}\n")
            with open('report_sold_tickets_by_sale_day.txt', 'a', encoding='utf-8') as file:
                file.write(f"Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) prodaje.\n")
                file.write(f"dan:{day}      datum:{date_choice}\n")
                file.write(table + "\n")
                file.write(
                    f"ukupan broj prodatih karata: {total_quantity}   ukupna cena prodatih karata:{total_price}\n")

    def sold_tickets_by_projection_term_day(self, day_choice):
        sold_tickets_controller = SoldTicketController()
        sold_tickets_controller.load_sold_tickets()
        list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets
        display_controller = DisplayController()
        date_choice = find_previous_date_by_day(int(day_choice))
        filtered_tickets = []
        for sold_ticket in list_of_sold_tickets:
            string_date = sold_ticket.ticket.projection_term.date.strftime("%d.%m.%Y.")
            if string_date == date_choice:
                filtered_tickets.append(sold_ticket)
        if not filtered_tickets:
            print("Nema pronađenih karata. Molimo pokušajte ponovo.")
        else:
            days = ['ponedeljak', 'utorak', 'sreda', 'četvrtak', 'petak', 'subota', 'nedelja']
            day = days[int(day_choice) - 1]
            table = display_controller.display_sold_tickets_by_projection_term_day(filtered_tickets)
            total_quantity = len(filtered_tickets)
            total_price = 0.0
            for sold_ticket in filtered_tickets:
                total_price += float(sold_ticket.price)

            print("Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije.\n")
            print(f"dan:{day}       datum:{date_choice}\n")
            print(table)
            print(f"ukupan broj prodatih karata: {total_quantity}   ukupna cena prodatih karata:{total_price}\n")
            with open('report_sold_tickets_by_projection_term_day.txt', 'a', encoding='utf-8') as file:
                file.write(
                    f"Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije.\n")
                file.write(f"dan:{day}      datum:{date_choice}\n")
                file.write(table + "\n")
                file.write(
                    f"ukupan broj prodatih karata: {total_quantity}   ukupna cena prodatih karata:{total_price}\n")

    def total_price_for_sold_tickets_by_movie(self, movie):
        sold_tickets_controller = SoldTicketController()
        sold_tickets_controller.load_sold_tickets()
        list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets
        display_controller = DisplayController()
        movie_title = movie.title
        print(movie_title)
        filtered_tickets = []
        for sold_ticket in list_of_sold_tickets:
            print(sold_ticket.ticket.projection_term.movie_projection.movie)
            if sold_ticket.ticket.projection_term.movie_projection.movie == movie_title:
                filtered_tickets.append(sold_ticket)
        if not filtered_tickets:
            print("Nema pronađenih karata. Molimo pokušajte ponovo.")
        else:
            table = display_controller.display_total_price_for_sold_tickets_by_movie(movie_title, filtered_tickets)
            print("Ukupna cena prodatih karata za zadati film u svim projekcijama")
            print(f"film: {movie_title}\n")
            print(table)
            with open('report_total_prise_for_sold_tickets_by_movie.txt', 'a', encoding='utf-8') as file:
                file.write("Ukupna cena prodatih karata za zadati film u svim projekcijama\n")
                file.write(f"film: {movie_title}\n")
                file.write(table + "\n")

    def sold_tickets_by_sale_day_and_sellperson(self, day_choice, sellperson_choice):
        sold_tickets_controller = SoldTicketController()
        sold_tickets_controller.load_sold_tickets()
        list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets
        display_controller = DisplayController()
        date_choice = find_previous_date_by_day(int(day_choice))
        filtered_tickets = []
        for sold_ticket in list_of_sold_tickets:
            string_date = sold_ticket.ticket.date.strftime("%d.%m.%Y.")
            if string_date == date_choice and sellperson_choice == sold_ticket.sellperson:
                filtered_tickets.append(sold_ticket)
        if not filtered_tickets:
            print("Nema pronađenih karata. Molimo pokušajte ponovo.")
        else:
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            day = days[int(day_choice) - 1]
            table = display_controller.sold_tickets_by_sale_day_and_sellperson(day, date_choice, sellperson_choice,
                                                                               filtered_tickets)

            print("Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca\n")
            print(table)
            with open('report_sold_tickets_by_sale_day_and_sellperson.txt', 'a', encoding='utf-8') as file:
                file.write(f"Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca\n")
                file.write(table + "\n")

    def sold_tickets_for_each_sellperson_in_last_30_days(self):
        user_controller = UserController()
        user_controller.load_users()
        list_of_users = user_controller.list_of_users
        display_controller = DisplayController()
        selpersons_usernames = []
        for user in list_of_users:
            if user.role == "2":
                selpersons_usernames.append(user.username)

        start_date = datetime.now() - timedelta(days=30)
        sold_tickets_data = []
        i = 0
        for sellperson in selpersons_usernames:
            i += 1
            filtered_list = sold_tickets_for_sellperson_in_last_30_days(sellperson, start_date)
            total_count = len(filtered_list)
            total_price = 0.0
            if filtered_list:
                for ticket_item in filtered_list:
                    total_price += float(ticket_item.price)

                sold_tickets_data.append([
                    i, sellperson, total_price, total_count
                ])
            else:
                sold_tickets_data.append([
                    i, sellperson, 0, 0
                ])

        table = display_controller.sold_tickets_for_each_sellperson_in_last_30_days(sold_tickets_data)
        print("Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakogprodavca) u poslednjih 30 dana\n")
        print(f"period: {start_date.date()} - {datetime.now().date()}")
        print(table)
        with open('sold_tickets_for_each_sellperson_in_last_30_days.txt', 'a', encoding='utf-8') as file:
            file.write(
                f"Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakogprodavca) u poslednjih 30 dana.\n")
            file.write(f"period: {start_date.date()} - {datetime.now().date()}")
            file.write(table + "\n")


def sold_tickets_for_sellperson_in_last_30_days(sellperson, start_date):
    sold_tickets_controller = SoldTicketController()
    sold_tickets_controller.load_sold_tickets()
    list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets
    last_date = datetime.now()
    filtered_list = []
    for sold_ticket in list_of_sold_tickets:
        if start_date <= sold_ticket.ticket.date <= last_date and sellperson == sold_ticket.sellperson:
            filtered_list.append(sold_ticket)
    return filtered_list


def find_previous_date_by_day(day_index):
    current_date = datetime.now()
    current_day = current_date.weekday()

    target_day = day_index - 1
    day_difference = (current_day - target_day) % 7
    if day_difference == 0:
        day_difference = 7

    previous_date = current_date - timedelta(days=day_difference)

    return previous_date.strftime('%d.%m.%Y.')
