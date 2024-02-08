import random
from datetime import datetime, timedelta
from CinemaHall import CinemaHall
from CinemaHallController import CinemaHallController
from DisplayController import DisplayController
from Movie import Movie
from MovieController import MovieController
from MovieCriterion import MovieCriterion
from MovieProjection import MovieProjection
from MovieProjectionController import MovieProjectionController
from MovieProjectionTerm import MovieProjectionTerm
from MovieProjectionTermController import MovieProjectionTermController
from MovieProjectionTermCriterion import MovieProjectionTermCriterion
from ReportController import ReportController
from SoldTicket import SoldTicket
from SoldTicketController import SoldTicketController
from Ticket import Ticket
from TicketController import TicketController, update_ticket_in_file
from TicketCriterion import TicketCriterion
from User import User
from UserController import UserController
from tabulate import tabulate

from ValidationController import ValidationController

current_user = None


def display_menu():
    print("MENI")
    print("_____")
    print("Izaberite opciju:")
    print("1. Registrujte se")
    print("2. Prijavite se")
    print("3. Izlaz iz aplikacije")
    print("4. Pregled dostupnih filmova")
    print("5. Pretraga filmova")
    print("6. Višestruka pretraga filmova")
    print("7. Pretraga termina bioskopskih projekcija")
    choice = input("Unesite broj opcije: ")
    print()
    return choice


def display_user_menu():
    global current_user
    if current_user is None:
        print("Niste prijavljeni.")
        return
    choice = str(current_user.role)
    if choice == "0":
        display_menu_for_admin()
    elif choice == "1":
        display_menu_for_registered_customer()
    elif choice == "2":
        display_menu_for_registered_salesperson()
    else:
        display_menu_for_registered_menager()


def display_menu_for_registered_customer():
    while True:
        print("MENI KORISNIKA")
        print("_______________")
        print("IZABERITE OPCIJU:")
        print("1. Odjava sa sistema: ")
        print("2. Izmena ličnih podataka")
        print("3. Izlaz iz aplikacije")
        print("4. Pregled dostupnih filmova")
        print("5. Pretraga filmova")
        print("6. Višestruka pretraga filmova")
        print("7. Pretraga termina bioskopskih projekcija")
        print("8. Rezervacija karte")
        print("9. Pregled rezervisanih karata")
        print("10. Poništavanje rezervacije karata")
        choice = input("Unesite broj opcije: ")
        if choice == "1":
            log_out()
        elif choice == "2":
            change_personal_information()
        elif choice == "3":
            exit_application()
        elif choice == "4":
            display_available_movies()
        elif choice == "5":
            search_movies()
        elif choice == "6":
            multi_search_movies()
        elif choice == "7":
            search_movie_projection_terms()
        elif choice == "8":
            reserve_ticket()
        elif choice == "9":
            display_reserved_tickets_for_user()
        elif choice == "10":
            cancellation_of_ticket_reservation()
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")


def display_menu_for_registered_salesperson():
    while True:
        print("MENI PRODAVCA")
        print("______________")
        print("Izaberite opciju:")
        print("1. Odjava sa sistema: ")
        print("2. Izmena ličnih podataka")
        print("3. Izlaz iz aplikacije")
        print("4. Pregled dostupnih filmova")
        print("5. Pretraga filmova")
        print("6. Višestruka pretraga filmova")
        print("7. Pretraga termina bioskopskih projekcija")
        print("8. Rezervacija karte")
        print("9. Prikaz rezervisanih karata")
        print("10. Poništavanje rezervisanih/prodatih karata")
        print("11. Pretraga karata")
        print("12. Direktna prodaja karte")
        print("13. Prodaja rezervisane karte")
        print("14. Izmena karte")
        choice = input("Unesite broj opcije: ")
        if choice == "1":
            log_out()
        elif choice == "2":
            change_personal_information()
        elif choice == "3":
            exit_application()
        elif choice == "4":
            display_available_movies()
        elif choice == "5":
            search_movies()
        elif choice == "6":
            multi_search_movies()
        elif choice == "7":
            search_movie_projection_terms()
        elif choice == "8":
            reserve_tickets_for_salesperson()
        elif choice == "9":
            display_reserved_tickets_for_sellperson()
        elif choice == "10":
            cancellation_of_ticket_for_sellperson()
        elif choice == "11":
            search_ticket()
        elif choice == "12":
            direct_sale_ticket_for_salesperson()
        elif choice == "13":
            sale_of_reserved_tickets()
        elif choice == "14":
            change_ticket_information()
        elif choice == "15":
            check_and_cancel_reservations()
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")


def display_menu_for_registered_menager():
    while True:
        print("MENI MENADŽERA")
        print("______________")
        print("Izaberi opciju:")
        print("1. Odjava sa sistema: ")
        print("2. Izmena ličnih podataka")
        print("3. Izlaz iz aplikacije")
        print("4. Registracija novih prodavaca")
        print("5. Registracija novih menadžera")
        print("6. Pregled dostupnih filmova")
        print("7. Pretraga filmova")
        print("8. Višestruka pretraga filmova")
        print("9. Pretraga termina bioskopskih projekcija")
        print("10. Izvestaji")
        print("11. Registracija filma")
        print("12. Izmena filma")
        print("13. Brisanje filma")
        print("14. Registracija bioskopske projekcije")
        print("15. Izmena bioskopske projekcije")
        print("16. Brisanje bioskopske projekcije")
        choice = input("Unesite broj opcije: ")
        if choice == "1":
            log_out()
        elif choice == "2":
            change_personal_information()
        elif choice == "3":
            exit_application()
        elif choice == "4":
            registrate_new_sellperson()
        elif choice == "5":
            registrate_new_menager()
        elif choice == "6":
            display_available_movies()
        elif choice == "7":
            search_movies()
        elif choice == "8":
            multi_search_movies()
        elif choice == "9":
            search_movie_projection_terms()
        elif choice == "10":
            create_report()
        elif choice == "11":
            registration_new_movie()
        elif choice == "12":
            update_movie()
        elif choice == "13":
            remove_movie()
        elif choice == "14":
            registration_new_movie_projection()
        elif choice == "15":
            update_projection()
        elif choice == "16":
            remove_projection()
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")


def display_menu_for_admin():
    print("MENI ADMINA")
    print("___________")
    print("1. Odjava sa sistema: ")
    print("2. Izlaz iz aplikacije")
    print("3. Registracija novih prodavaca")
    print("4. Registracija novih menadžera")
    print("5. Registracija filma")
    print("6. Izmena filma")
    print("7. Brisanje filma")
    print("8. Registracija bioskopske projekcije")
    print("9. Izmena bioskopske projekcije")
    print("10. Brisanje bioskopske projekcije")
    print("11. Registracija sale za projekcije")
    print("12. Registracija termina bioskopske projekcije")
    choice = input("Unesi broj opcije: ")

    if choice == "1":
        log_out()
    elif choice == "2":
        exit_application()
    elif choice == "3":
        registrate_new_sellperson()
    elif choice == "4":
        registrate_new_menager()
    elif choice == "5":
        registration_new_movie()
    elif choice == "6":
        update_movie()
    elif choice == "7":
        remove_movie()
    elif choice == "8":
        registration_new_movie_projection()
    elif choice == "9":
        update_projection()
    elif choice == "10":
        remove_projection()
    elif choice == "11":
        registration_new_cinemahall()
    elif choice == "12":
        registration_new_movie_projection_term()
    else:
        print("Nevažeća opcija. Molimo pokušajte ponovo.")



def display_projection_(list):
    if not list:
        print("Nema ponuđenih termina projekcija")
    else:
        i = 1
        for projection_term in list:
            print(f"PROJEKCIJA {i}")
            projection_term.display_movie_projection()
            i += 1
            print()


def display_available_movies():
    print("PRIKAZ DOSTUPNIH FILMOVA")
    print("________________________")
    display_controller.display_movies()


def display_reserved_tickets_for_user():
    username = current_user.username
    user_reserved_ticket = []
    for ticket in ticket_controller.list_of_tickets:
        if ticket.owner == username and ticket.status == "1":
            user_reserved_ticket.append(ticket)

    if not user_reserved_ticket:
        print("Nema rezervisanih karti.")
        return None
    else:
        display_controller.display_reserved_tickets_for_user(user_reserved_ticket)
        return user_reserved_ticket


def display_reserved_tickets_for_sellperson():
    display_controller.display_reserved_tickets()


def login():
    global current_user
    print("PRIJAVA")
    print("_______")
    print("Za povratak na meni unesite: -1")
    while True:
        username = input("Unesite korisničko ime: ")
        if username == "-1":
            main()
            return
        password = input("Unesite lozinku: ")
        if password == "-1":
            main()
            return
        if user_controller.authenticate_user(username, password):
            print("Uspešno ste se prijavili!")
            current_user = user_controller.get_user(username)
            display_user_menu()
        else:
            target_user = user_controller.get_user(username)
            if target_user is None:
                print("Uneto je pogrešno korisničko ime. Molimo pokušajte ponovo.")
            else:
                print("Uneta je pogrešna lozinka. Molimo pokušajte ponovo.")


def log_out():
    global current_user
    current_user = None
    print("Uspešno ste se odjavili.")
    print()
    main()


def exit_application():
    print("Hvala što ste koristili aplikaciju. Doviđenja!")
    exit()


def change_personal_information():
    global current_user
    print("IZMENA LIČNIH INFORMACIJA")
    print("_______________________")
    while True:
        print("Za povratak na meni unesite: -1")
        print("1. Ime")
        print("2. Prezime")
        print("3. Lozinka")
        choice = input("Unesite broj opcije: ")

        if choice == "-1":
            display_user_menu()
            return

        elif choice == "1":
            new_name = input("Unesite novo ime:")
            if new_name == "-1":
                continue
            elif not validation_controller.user_valid_name(new_name):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.name = new_name
                if user_controller.update_user_in_list(current_user):
                    print('Uspešno ste izmenili ime.')
                    current_user.display_user()
                else:
                    print("Niste uspešno izmenili ime. Molimo pokušajte ponovo.")

        elif choice == "2":
            new_surname = input("Unesite novo prezime:")
            if new_surname == "-1":
                continue
            if not validation_controller.user_valid_surname(new_surname):
                print("Nevažeće prezime. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.surname = new_surname
                if user_controller.update_user_in_list(current_user):
                    print('Usepšno ste izmenili prezime.')
                    current_user.display_user()
                else:
                    print("Niste uspešno promenili prezime. Molimo pokušajte ponovo.")

        elif choice == "3":
            new_password = input("Unesite novu lozinku (minimum 6 karaktera sa bar jednom cifrom): ")
            if new_password == "-1":
                continue
            if not validation_controller.user_valid_password(new_password):
                print("Nevažeća lozinka. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.password = new_password
                if user_controller.update_user_in_list(current_user):
                    print('Usepšno ste izmenili lozinku.')
                    current_user.display_user()
                else:
                    print("Niste uspešno promenili lozinku. Molimo polušajte ponovo.")
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")
    print()


def registration():
    global current_user
    print("REGISTRACIJA")
    print("____________")
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite Vaše korisničko ime: ")
        if username == '-1':
            main()
            return
        elif not validation_controller.user_valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite željenu lozinku: ")
        if password == '-1':
            main()
            return
        elif not validation_controller.user_valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite Vaše ime: ")
        if name == '-1':
            main()
            return
        elif not validation_controller.user_valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite Vaše prezime: ")
        if surname == '-1':
            main()
            return
        elif not validation_controller.user_valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue

        role = 1
        new_user = User(username, password, name, surname, role)
        current_user = new_user
        if user_controller.add_user(new_user):
            print("Uspešno ste se registrovali!")
            display_user_menu()
            break
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")
    print()


def registrate_new_sellperson():
    print("REGISTRACIJA NOVOG PRODAVCA")
    print("___________________________")
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite korisničko ime: ")

        if username == "-1":
            display_user_menu()
            return
        elif not validation_controller.user_valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite lozinku: ")
        if password == "-1":
            continue
        elif not validation_controller.user_valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite ime: ")
        if name == "-1":
            continue
        elif not validation_controller.user_valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite prezime: ")
        if surname == "-1":
            continue
        elif not validation_controller.user_valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue

        role = 2

        registrate_new_sellperson = User(username, password, name, surname, role)
        if user_controller.add_user(registrate_new_sellperson):
            print("Uspešno ste registrovali novog prodavca")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def registrate_new_menager():
    print("REGISTRACIJA NOVOG MENADŽERA")
    print("____________________________")
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite korisničko ime: ")
        if username == "-1":
            display_user_menu()
            return
        elif not validation_controller.user_valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite lozinku: ")
        if password == "-1":
            continue
        elif not validation_controller.user_valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite ime: ")
        if name == "-1":
            continue
        elif not validation_controller.user_valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite prezime: ")
        if surname == "-1":
            continue
        elif not validation_controller.user_valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue
        role = 3

        registrate_new_sellperson = User(username, password, name, surname, role)
        if user_controller.add_user(registrate_new_sellperson):
            print("Uspešno ste registrovali novog menadžera.")
            continue
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def registration_new_movie_projection():
    list_of_movie_projection = movie_projection_controller.list_of_projections
    list_of_cinema_hall = cinema_hall_controller.list_of_cinema_halls
    list_of_movie = movie_controller.list_of_movies
    print("REGISTRACIJA NOVE FILMSE PROJEKCIJE")
    print("___________________________________")
    while True:
        print("Unesite -1 za povratak nazad")
        projection_code_choice = input("Unesite kod projekcije: ")
        projection_code = projection_code_choice
        if projection_code_choice == "-1":
            display_user_menu()
            return
        elif not MovieProjection.valid_code(projection_code_choice):
            print("Nevažeći kod. Molimo pokušajte ponovo.")
            continue
        else:
            for movie_projection in list_of_movie_projection:
                if movie_projection.projection_code == projection_code_choice:
                    print("Kod već postoji. Molimo pokušajte ponovo")
                    projection_code = None

            if projection_code is None:
                continue

        hall = None
        print("IZBOR SALE")
        print("__________")
        for cinema_hall in list_of_cinema_hall:
            print(f"- {cinema_hall.hall_code}")
        hall_code = input("Unesite kod sale: ")
        if hall_code == "-1":
            continue
        elif not CinemaHall.valid_hall_code(hall_code):
            print("Nevažeći kod. Molimo pokušajte ponovo.")
            continue
        else:
            for cinema_hall in list_of_cinema_hall:
                if cinema_hall.hall_code == hall_code:
                    hall = cinema_hall

            if hall is None:
                print("Nije pronađena sala sa odgovarajućim kodom. Molimo pokušajte ponovo.")
                continue

        start_time = input("Unesite vreme početka projekcije: ")
        if start_time == "-1":
            continue
        elif not MovieProjection.valid_time_format(start_time):
            print("Nevažeće vreme. Molimo pokušajte ponovo.")
            continue

        end_time = input("Unesite vreme kraja projekcije: ")
        if end_time == "-1":
            continue
        elif not MovieProjection.valid_time_format(end_time):
            print("Nevažeće vreme. Molimo pokušajte ponovo.")
            continue

        projection_days = input("Unesite dane projekcije: ")
        if projection_days == "-1":
            continue
        elif not MovieProjection.valid_day_input(projection_days):
            print("Nevažeći unos dana projekcije. Molimo pokušajte ponovo")
            continue

        movie = None
        print("IZBOR FILMA")
        print("___________")
        for movie_item in list_of_movie:
            print(f"- {movie_item.title}")
        projection_movie = input("Unesite ime film: ")
        if projection_movie == "-1":
            continue
        elif not Movie.valid_name(projection_movie):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue
        else:
            for movie_item in list_of_movie:
                if movie_item.title == projection_movie:
                    movie = movie_item

            if movie is None:
                print("Nije pronađen film sa odgovarajućim imenom. Molimo pokušajte ponovo.")
                continue

        price = input("Unesite osnovnu cenu karte: ")
        if price == "-1":
            continue
        elif not MovieProjection.valid_price(price):
            print("Nevažeća cena. Molimo pokušajte ponovo.")
            continue

        new_projection = MovieProjection(projection_code, hall, start_time, end_time,
                                         projection_days, projection_movie, price)
        if movie_projection_controller.add_projection(new_projection):
            print("Uspešno ste registrovali novu projekciju")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def update_projection():
    while True:
        display_controller.display_projections()
        choice = input("Unesite opciju: ")
        if choice == "-1":
            display_user_menu()
            return
        if not (1 <= int(choice) <= len(movie_projection_controller.list_of_projections)):
            print("Nevažeća opcija. Molimo pokušajte kasnije.")
            continue
        else:
            projection = movie_projection_controller.list_of_projections[int(choice) - 1]
            projection_copy = projection.make_copy()
            print("IZMENA PROJEKCIJE")
            print("_________________")
            print("Za povratak na meni unesite: -1")
            print("1. Sala")
            print("2. Vreme početka")
            print("3. Vreme kraja")
            print("4. Dani projekcije")
            print("5. Film")
            print("6. Cena")
            choice = input("Unesite opciju: ")

            if choice == "-1":
                continue
            if choice == "1":
                display_controller.display_cinema_halls()
                new_hall_code = input("Unesite nov kod sale: ")
                if new_hall_code.strip() != "":
                    if not CinemaHall.valid_hall_code(new_hall_code):
                        print("Nevažeći kod sale. Molimo pokušajte ponovo.")
                        continue
                    else:
                        for cinema_hall in cinema_hall_controller.list_of_cinema_halls:
                            if cinema_hall.hall_code == new_hall_code:
                                projection.hall = cinema_hall
                                if movie_projection_controller.update_projection(projection_copy, projection):
                                    print("Uspešno ste izmenili cenu.")
                                    continue
                        else:
                            print("Sala sa datim kodom nije pronađena. Molimo pokušajte ponovo.")
                            continue
            if choice == "2":
                new_start_time = input("Unesite novo vreme početka: ")
                if new_start_time.strip() != "":
                    if not MovieProjection.valid_time_format(new_start_time):
                        print("Nevažeće vreme početka. Molimo pokušajte ponovo.")
                        continue
                    else:
                        projection.start_time = new_start_time
                        if movie_projection_controller.update_projection(projection_copy, projection):
                            print("Uspešno ste izmenili cenu.")
                            continue
            if choice == "3":
                new_end_time = input("Unesite novo vreme kraja: ")
                if new_end_time.strip() != "":
                    if not MovieProjection.valid_time_format(new_end_time):
                        print("Nevažeće vreme kraja. Molimo pokušajte ponovo.")
                        continue
                    else:
                        projection.end_time = new_end_time
                        if movie_projection_controller.update_projection(projection_copy, projection):
                            print("Uspešno ste izmenili cenu.")
                            continue
            if choice == "4":
                new_days = input("Unesite nove dane projekcije: ")
                if new_days.strip() != "":
                    if not MovieProjection.valid_day_input(new_days):
                        print("Nevažeći unos dana projekcije. Molimo pokušajte ponovo.")
                        continue
                    else:
                        projection.projection_days = new_days
                        if movie_projection_controller.update_projection(projection_copy, projection):
                            print("Uspešno ste izmenili cenu.")
                            continue
            if choice == "5":
                display_controller.display_movies()
                new_movie_title = input("Unesite novi naslov filma: ")
                if new_movie_title.strip() != "":
                    for movie in movie_controller.list_of_movies:
                        if movie.title == new_movie_title:
                            projection.movie = movie
                            if movie_projection_controller.update_projection(projection_copy, projection):
                                print("Uspešno ste izmenili cenu.")
                            continue
                    else:
                        print("Film sa datim naslovom nije pronađen. Molimo pokušajte ponovo.")
                        continue
            if choice == "6":
                new_price = input("Unesite novu cenu: ")
                if new_price.strip() != "":
                    if not MovieProjection.valid_price(new_price):
                        print("Nevažeća cena. Molimo pokušajte ponovo.")
                        continue
                    else:
                        projection.price = new_price
                        if movie_projection_controller.update_projection(projection_copy, projection):
                            print("Uspešno ste izmenili cenu.")
                            continue


def remove_projection():
    while True:
        display_controller.display_projection()
        choice = input("Unesite broj izabrane projekcije:")
        if choice == "-1":
            display_user_menu()
            return
        elif not (1 <= int(choice) <= len(movie_projection_controller.list_of_projections)):
            print("Pogrešan unos. Molimo pokušajte ponovo.")
            continue
        else:
            delete = True
            projection_choice = movie_projection_controller.list_of_projections[int(choice) - 1]
            for ticket in ticket_controller.list_of_tickets:
                if (ticket.projection_term.movie_projection.movie == projection_choice.movie and
                        ticket.projection_term.date > datetime.now().date()):
                    delete = False
                    break
            if delete:
                delete_projection_term_list = []
                for projection_term in movie_projection_term_controller.list_of_projection_terms:
                    if (projection_term.movie_projection.movie == projection_choice.movie and
                            projection_term.movie_projection.projection_code == projection_choice.projection_code
                            and projection_term.movie_projection.hall == projection_choice.hall and
                            projection_term.movie_projection.start_time == projection_choice.start_time and
                            projection_term.movie_projection.end_time == projection_choice.end_time and
                            projection_term.movie_projection.projection_days == projection_choice.projection_days
                            and projection_term.movie_projection.ticket_price == projection_choice.ticket_price):
                        delete_projection_term_list.append(projection_term)
                movie_projection_term_controller.remove_projection_terms(delete_projection_term_list)

                delete_projection = []
                for projection in movie_projection_controller.list_of_projections:
                    if (projection.movie == projection_choice.movie and
                            projection.projection_code == projection_choice.projection_code
                            and projection.hall == projection_choice.hall and
                            projection.start_time == projection_choice.start_time and
                            projection.end_time == projection_choice.end_time and
                            projection.projection_days == projection_choice.projection_days
                            and projection.ticket_price == projection_choice.ticket_price):
                        delete_projection.append(projection)
                movie_projection_controller.remove_projections(delete_projection)
            else:
                print("Trenutno postoje važeće karte. Molimo pokušajte kasnije.")
                continue


def generate_new_projection_terms():
    current_date = datetime.now().date()
    for i in range(7):
        first_date = current_date + timedelta(days=i)
        second_date = first_date + timedelta(days=7)
        day_in_week = MovieProjectionTermController.get_day_of_week(first_date)
        for projection in movie_projection_controller.list_of_projections:
            if day_in_week in projection.projection_days:
                index = MovieProjectionTermController.generate_index(projection)
                first_projection_term = MovieProjectionTerm(projection, index, first_date)
                second_projection_term = MovieProjectionTerm(projection, index, second_date)
                MovieProjectionTermController.add_projection_term(first_projection_term)
                MovieProjectionTermController.add_projection_term(second_projection_term)


def registration_new_cinemahall():
    list_of_cinema_hall = cinema_hall_controller.list_of_cinema_halls
    print("REGISTRACIJA NOVE BIOSKOPSKE SALE")
    print("_________________________________")
    while True:
        print("Unesite -1 za povratak u nazad")
        hall_code_choice = input("Unesite kod sale: ")
        hall_code = hall_code_choice
        if hall_code_choice == "-1":
            display_user_menu()
        elif not CinemaHall.valid_hall_code(hall_code_choice):
            print("Nevažeći kod. Molimo pokušajte ponovo.")
            continue
        else:
            for cinemahall in list_of_cinema_hall:
                if cinemahall.hall_code == hall_code_choice:
                    print("Kod već postoji. Molimo pokušajte ponovo.")
                    hall_code = None

            if hall_code is None:
                continue

        hall_name_choice = input("Unesite ime sale:")
        hall_name = hall_name_choice
        if hall_name_choice == "-1":
            continue
        elif not CinemaHall.valid_cinema_hall_name(hall_name_choice):
            print("Nevažeće ime. Molimo pokušajte ponovo")
            continue
        else:
            for cinemahall in list_of_cinema_hall:
                if cinemahall.hall_name == hall_name_choice and hall_name_choice != "None":
                    print("Ime već postoji. Molimo pokušajte ponovo.")
                    hall_name = None

            if hall_name is None:
                continue

            if hall_name_choice == "None":
                hall_name = None

        num_rows_choice = input("Unesite broj redova: ")
        num_rows = None
        if num_rows_choice == "-1":
            continue
        elif not CinemaHall.valid_num_rows(num_rows_choice):
            print("Nevažeći broj redova. Molimo pokušajte ponovo.")
            continue
        else:
            num_rows = num_rows_choice

        seat_labels_choice = input("Unesite oznake sedišta: ")
        seat_labels = None
        if seat_labels_choice == "-1":
            continue
        elif not CinemaHall.valid_seat_labels(seat_labels_choice):
            print("Nevažeće oznake. Molimo pokušajte ponovo.")
            continue
        else:
            seat_labels = seat_labels_choice

        new_cinemahall = CinemaHall(hall_code, num_rows, seat_labels, hall_name)

        if cinema_hall_controller.add_hall(new_cinemahall):
            print("Uspešno ste registrovali novu salu")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def registration_new_movie():
    print("REGISTRACIJA NOVOG FILMA")
    print("________________________")
    while True:
        print("Unesite -1 za povratak nazad")
        title = input("Unesite naziv filma: ")
        if title == "-1":
            display_user_menu()
        elif not validation_controller.movie_valid_name(title):
            print("Nevažeći naziv filma. Molimo pokušajte ponovo.")
            continue
        genre = input("Unesite žanr filma: ")
        if genre == "-1":
            continue
        elif not validation_controller.movie_valid_genre(genre):
            print("Nevažeći žanr. Molimo pokušajte ponovo.")
            continue
        duration = input("Unesite trajanje filma (u minutama): ")
        if duration == "-1":
            continue
        elif not validation_controller.movie_valid_duration(duration):
            print("Nevažeće trajanje filma. Molimo pokušajte ponovo.")
            continue

        director = input("Unesite ime reditelja: ")
        if director == "-1":
            continue
        elif not validation_controller.movie_valid_director(director):
            print("Nevažeće ime reditelja. Molimo pokušajte ponovo.")
            continue

        main_roles = input("Unesite glavne uloge: ")
        if main_roles == "-1":
            continue
        elif not validation_controller.movie_valid_main_roles(main_roles):
            print("Nevažeće ime glumca. Molimo pokušajte ponovo.")
            continue

        country_of_origin = input("Unesite zemlju porekla filma: ")
        if country_of_origin == "-1":
            continue
        elif not validation_controller.movie_valid_country_name(country_of_origin):
            print("Nevažeća zemlja porekla filma. Molimo pokušajte ponovo.")
            continue

        release_year = input("Unesite godinu izdanja filma: ")
        if release_year == "-1":
            continue
        elif not validation_controller.movie_valid_year(release_year):
            print("Nevažeća godina objave filma. Molimo pokušajte ponovo.")
            continue

        description = input("Unesite opis filma: ")
        if description == "-1":
            continue

        new_movie = Movie(title, genre, duration, director, main_roles, country_of_origin, release_year, description)

        if movie_controller.add_movie(new_movie):
            print("Uspešno ste registrovali novi film")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def update_movie():
    while True:
        display_controller.display_movies()
        choice = input("Unesite ID filma: ")
        if choice == "-1":
            display_user_menu()
            return
        if not (1 <= int(choice) <= len(movie_controller.list_of_movies)):
            print("Nevažeća opcija. Molimo pokušajte kasnije.")
            continue
        else:
            movie = movie_controller.list_of_movies[int(choice) - 1]
            movie_copy = movie.make_copy()
            print("IZMENA FILMA")
            print("___________")
            print("Za povratak na meni unesite: -1")
            print("1. Naziv")
            print("2. Žanrovi")
            print("3. Režiseri")
            print("4. Glavne uloge")
            print("5. Država porekla")
            print("6. Godina")
            print("7. Opis")
            print("8. Trajanje")
            print()
            choice = input("Unesite opciju: ")

            if choice == "1":
                new_title = input("Unesite nov naziv:")
                if new_title == "-1":
                    continue
                elif not validation_controller.movie_valid_name(new_title):
                    print("Nevazece ime. Molimo pokusajte ponovo.")
                    continue
                else:
                    movie.title = new_title
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspesno ste izmenili ime.")
                        continue

            if choice == "2":
                display_controller.display_genres()
                new_genres = input("Unesite nove žanrove: ")
                if new_genres == "-1":
                    continue
                elif validation_controller.movie_valid_genre(new_genres):
                    print("Nevažeći žanrovi. Molimo pokušajte ponovo.")
                    continue
                else:
                    movie.genre = new_genres
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspešno ste izmenili žanrove.")
                        continue

            if choice == "3":
                new_directors = input("Unesite nove režisere: ")
                if new_directors == "-1":
                    continue
                elif not validation_controller.movie_valid_director(new_directors):
                    print("Nevažće ime. Molimo pokušajte ponovo")
                    continue
                else:
                    movie.director = new_directors
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspešno ste izmenili direktore.")
                        continue

            if choice == "4":
                new_actors = input("Unesite nove glumce: ")
                if new_actors == "-1":
                    continue
                elif not validation_controller.movie_valid_main_roles(new_actors):
                    print("Nevažće ime. Molimo pokušajte ponovo")
                    continue
                else:
                    movie.main_roles = new_actors
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspešno ste izmenili glavne uloge.")
                        continue

            if choice == "5":
                new_country = input("Unesite novu državu porekla: ")
                if new_country == "-1":
                    continue
                elif not validation_controller.movie_valid_country_name(new_country):
                    print("Nevažće ime. Molimo pokušajte ponovo")
                    continue
                else:
                    movie.country_of_origin = new_country
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspešno ste izmenili državu.")
                        continue

            if choice == "6":
                new_year = input("Unesite novu godinu: ")
                if new_year == "-1":
                    continue
                elif not validation_controller.movie_valid_year(new_year):
                    print("Nevažća godina. Molimo pokušajte ponovo.")
                    continue
                else:
                    movie.release_year = new_year
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspešno ste izmenili žanrove.")
                        continue

            if choice == "7":
                new_description = input("Unesite nov opis: ")
                if new_description == "-1":
                    continue
                else:
                    movie.description = new_description
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspešno ste izmenili opis.")
                        continue

            if choice == "8":
                new_duration = input("Unesite novo trajanje u minutima: ")
                if new_duration == "-1":
                    continue
                elif not validation_controller.movie_valid_duration(new_duration):
                    print("Nevažeče trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    movie.duration = new_duration
                    if movie_controller.update_movie(movie_copy, movie):
                        print("Uspešno ste izmenili žanrove.")
                        continue




def remove_movie():
    while True:
        display_controller.display_movies()
        choice = input("Unesite broj izabranog filma:")
        if choice == "-1":
            display_user_menu()
            return
        elif not (1 <= int(choice) <= len(movie_controller.list_of_movies)):
            print("Pogrešan unos. Molimo pokušajte ponovo.")
            continue
        else:
            delete = True
            movie_choice = movie_controller.list_of_movies[int(choice) - 1]
            for ticket in ticket_controller.list_of_tickets:
                if (ticket.projection_term.movie_projection.movie == movie_choice.title and
                        ticket.projection_term.date > datetime.now().date()):
                    delete = False
                    break
            if delete:
                delete_projection_term_list = []
                for projection_term in movie_projection_term_controller.list_of_projection_terms:
                    if projection_term.movie_projection.movie == movie_choice.title:
                        delete_projection_term_list.append(projection_term)
                movie_projection_term_controller.remove_projection_terms(delete_projection_term_list)

                delete_projection = []
                for projection in movie_projection_controller.list_of_projections:
                    if projection.movie == movie_choice.title:
                        delete_projection.append(projection)
                movie_projection_controller.remove_projections(delete_projection)

                movie_controller.remove_movie(movie_choice)
            else:
                print("Trenutno postoje važeće karte. Molimo pokušajte kasnije.")
                continue


def registration_new_movie_projection_term():
    print("REGISTRACIJA NOVOG TERMINA PROJEKCIJE FILMA")
    print("__________________________________________")
    print("Unesite -1 za povratak nazad")
    list_of_projections = movie_projection_controller.list_of_projections
    display_projection_(list_of_projections)
    while True:
        index = None
        projection = None
        date_object = None
        projection_choice = int(input("Unesi broj izabrane projekcije: "))
        if projection_choice == -1:
            display_user_menu()
            return
        elif 0 <= projection_choice - 1 < len(list_of_projections):
            index = projection_choice - 1
            projection = list_of_projections[projection_choice - 1]
        else:
            print("Nevažeći indeks. Molimo pokušajte ponovo.")
            continue
        projection_term_date_choice = input("Unesi datum termina projekcije: ")
        if projection_term_date_choice == "-1":
            continue
        elif not MovieProjectionTerm.valid_date_format(projection_term_date_choice):
            print("Nevažeći format datuma. Molimo pokušajte ponovo: ")
            continue
        else:
            date_object = datetime.strptime(projection_term_date_choice, '%d.%m.%Y.').date()
            if movie_projection_term_controller.valid_date(projection, date_object):
                new_projection_term = MovieProjectionTerm(projection, index, date_object)
                if movie_projection_term_controller.add_projection_term(new_projection_term):
                    print("Uspešno ste registrovali novu projekciju")
                    display_user_menu()
                else:
                    print("Registracija nije uspela. Molimo pokušajte ponovo.")


def multi_search_movies():
    criteria = MovieCriterion()
    print("VIŠESTRUKA PRETRAGA")
    print("___________________")
    while True:
        print("Za povratak na meni unesite: -1")
        print("IZBOR KRITERIJUMA")
        print("1. Naziv")
        print("2. Žanr")
        print("3. Trajanje filma")
        print("4. Režiser")
        print("5. Glavne uloge")
        print("6. Zemlja porekla")
        print("7. Godina proizvodnje")
        print("0. Završi unos kriterijuma")

        choice = input("Unesite broj za kriterijum koji želite da unesete: ")

        if choice == "-1":
            if current_user is None:
                display_menu()
            else:
                display_user_menu()
                return

        elif choice == "0":
            break

        elif choice == "1":
            choice_title = input("Unesite naziv filma: ")
            if choice_title == "-1":
                continue
            elif not validation_controller.movie_valid_name(choice_title):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.title = choice_title

        elif choice == "2":
            display_controller.display_genres()
            choice_genre = input("Unesite žanr filma: ")
            if choice_genre == "-1":
                continue
            elif not validation_controller.movie_valid_genre(choice_genre):
                print("Nevažeći žanr. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.genre = choice_genre

        elif choice == "3":
            print("1. Maksimalno trajanje")
            print("2. Minimalno trajanje")
            print("3. Opseg trajanja")
            print("4. Tacno trajanje")
            duration_choice = input("Unesite opciju za trajanje filma: ")
            if duration_choice == "-1":
                continue

            if duration_choice == "1":
                max_duration_choice = input("Unesite maksimalno trajanje filma: ")
                if max_duration_choice == "-1":
                    continue
                elif not validation_controller.movie_valid_duration(max_duration_choice):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    criteria.max_duration = max_duration_choice

            elif duration_choice == "2":
                min_duration_choice = input("Unesite minimalno trajanje filma: ")
                if min_duration_choice == "-1":
                    continue
                elif not validation_controller.movie_valid_duration(min_duration_choice):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    criteria.min_duration = min_duration_choice

            elif duration_choice == "3":
                min_duration_choice = input("Unesite minimalno trajanje filma: ")
                max_duration_choice = input("Unesite maksimalno trajanje filma: ")
                if min_duration_choice == "-1" or max_duration_choice == "-1":
                    continue
                elif not (validation_controller.movie_valid_duration(min_duration_choice)
                          or validation_controller.movie_valid_duration(max_duration_choice)):
                    if int(min_duration_choice) > int(max_duration_choice):
                        print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                        continue
                else:
                    criteria.min_duration = min_duration_choice
                    criteria.max_duration = max_duration_choice

            elif duration_choice == "4":
                duration_choice = input("Unesite tačno trajanje filma: ")
                if duration_choice == '-1':
                    continue
                elif not validation_controller.movie_valid_duration(duration_choice):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    criteria.duration = duration_choice
            else:
                print("Nevažeći unos za trajanje filma. Molimo pokušajte ponovo.")
                continue

        elif choice == "4":
            choice_director = input("Unesite ime režisera: ")
            if choice_director == "-1":
                continue
            elif not validation_controller.movie_valid_director(choice_director):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.director = choice_director

        elif choice == "5":
            main_roles_choice = input("Unesite glavne uloge: ")
            if main_roles_choice == "-1":
                continue
            if not validation_controller.movie_valid_main_roles(main_roles_choice):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.main_roles = main_roles_choice

        elif choice == "6":
            country_choice = input("Unesite zemlju porekla: ")
            if country_choice == "-1":
                continue
            elif not validation_controller.movie_valid_country_name(country_choice):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.country_of_origin = country_choice

        elif choice == "7":
            year_choice = input("Unesite godinu proizvodnje: ")
            if year_choice == "-1":
                continue
            elif not validation_controller.movie_valid_year(year_choice):
                print("Nevažeća godina. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.release_year = year_choice
        else:
            print("Nevažeći unos. Molimo pokušajte ponovo.")
            continue

    filtered_list = movie_controller.search(criteria)
    display_controller.display_filtered_movies(filtered_list)


def search_movies():
    print("PRETRAGA FILMOVA")
    print("________________")
    while True:
        print("Za povratak na meni unesite: -1")
        print("1. Naziv")
        print("2. Žanr")
        print("3. Trajanje filma")
        print("4. Režiser")
        print("5. Glavne uloge")
        print("6. Zemlja porekla")
        print("7. Godina proizvodnje")
        choice = input("Izaberite kriterijum po kom želite da pretražite filmove: ")

        if choice == "-1":
            if current_user is None:
                display_menu()
            else:
                display_user_menu()
                return

        elif choice == "1":
            movie_name = input("Unesite naziv filma: ")
            if movie_name == "-1":
                continue
            elif movie_name.strip() == "":
                print("Niste uneli naziv filma.")
                continue
            elif not validation_controller.movie_valid_name(movie_name):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                name_criterion = MovieCriterion(title=movie_name)
                filtered_list = movie_controller.search(name_criterion)
                if not filtered_list:
                    print("Nema pronađenih filmova")
                else:
                    display_controller.display_filtered_movies(filtered_list)

        elif choice == "2":
            display_controller.display_genres()
            movie_genre = input("Unesite naziv žanra: ")
            if movie_genre == "-1":
                continue
            elif movie_genre.strip() == "":
                print("Niste uneli naziv žanra.")
                continue
            elif not validation_controller.movie_valid_genre(movie_genre):
                print("Nevažeći žanr. Molimo pokušajte ponovo.")
                continue
            else:
                genre_criterion = MovieCriterion(genre=movie_genre)
                filtered_list = movie_controller.search(genre_criterion)
                if not filtered_list:
                    print("Nema pronađenih filmova.")
                else:
                    display_controller.display_filtered_movies(filtered_list)

        elif choice == "3":
            print("Za povratak na meni unesite: -1")
            print("1.Maksimalno trajanje")
            print("2.Minimalno trajanje")
            print("3. Opseg trajanja")
            print("4. Tacno trajanje ")
            choice = input("Izaberi opciju pretrage trajanja filma: ")

            if choice == '-1':
                continue

            elif choice == '1':
                max_movie_duration = input("Unesite maksimalno trajanje filma u minutima: ")
                if max_movie_duration == '-1':
                    continue
                elif max_movie_duration.strip() == "":
                    print("Niste uneli trajanje filma.")
                    continue
                elif not validation_controller.movie_valid_duration(max_movie_duration):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    max_movie_duration_criterion = MovieCriterion(max_duration=max_movie_duration)
                    filtered_list = movie_controller.search(max_movie_duration_criterion)
                    if not filtered_list:
                        print("Nema pronađenih filmova.")
                    else:
                        display_controller.display_filtered_movies(filtered_list)

            elif choice == '2':
                min_movie_duration = input("Unesite minimalno trajanje filma u minutima: ")
                if min_movie_duration == '-1':
                    continue
                elif min_movie_duration.strip() == "":
                    print("Niste uneli trajanje filma.")
                    continue
                elif not validation_controller.movie_valid_duration(min_movie_duration):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    min_movie_duration_criterion = MovieCriterion(min_duration=min_movie_duration)
                    filtered_list = movie_controller.search(min_movie_duration_criterion)
                    if not filtered_list:
                        print("Nema pronađenih filmova.")
                    else:
                        display_controller.display_filtered_movies(filtered_list)

            elif choice == '3':
                max_movie_duration = input("Unesite maksimalno trajanje filma u minutima: ")
                min_movie_duration = input("Unesite minimalno trajanje filma u minutima: ")
                if max_movie_duration == '-1' or min_movie_duration == '-1':
                    continue
                elif min_movie_duration.strip() == "" or max_movie_duration.strip() == "":
                    print("Niste uneli trajanje filma.")
                    continue
                elif not (validation_controller.movie_valid_duration(min_movie_duration) or
                          validation_controller.movie_valid_duration(max_movie_duration)):
                    if int(max_movie_duration) < int(min_movie_duration):
                        print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                        continue
                else:
                    movie_duration_range_criterion = MovieCriterion(min_duration=min_movie_duration,
                                                                    max_duration=max_movie_duration)
                    filtered_list = movie_controller.search(movie_duration_range_criterion)
                    if not filtered_list:
                        print("Nema pronađenih filmova.")
                    else:
                        display_controller.display_filtered_movies(filtered_list)

            elif choice == '4':
                movie_duration = input("Unesite trajanje filma u minutima: ")
                if movie_duration == "-1":
                    continue
                elif movie_duration.strip() == "":
                    print("Niste uneli trajanje filma.")
                    continue
                elif not validation_controller.movie_valid_duration(movie_duration):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    movie_duration_criterion = MovieCriterion(duration=movie_duration)
                    filtered_list = movie_controller.search(movie_duration_criterion)
                    if not filtered_list:
                        print("Nema pronađenih filmova.")
                    else:
                        display_controller.display_filtered_movies(filtered_list)

        elif choice == "4":
            movie_director = input("Unesite ime režisera: ")
            if movie_director == "-1":
                continue
            elif movie_director.strip() == "":
                print("Niste uneli režisera.")
                continue
            elif not validation_controller.movie_valid_director(movie_director):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                movie_director_criterion = MovieCriterion(director=movie_director)
                filtered_list = movie_controller.search(movie_director_criterion)
                if not filtered_list:
                    print("Nema pronađenih filmova.")
                else:
                    display_controller.display_filtered_movies(filtered_list)

        elif choice == "5":
            movie_actor = input("Unesite ime glumca: ")
            if movie_actor == "-1":
                continue
            elif movie_actor.strip() == "":
                print("Niste uneli glumca.")
                continue
            elif not validation_controller.movie_valid_main_roles(movie_actor):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                movie_actor_criterion = MovieCriterion(main_roles=movie_actor)
                filtered_list = movie_controller.search(movie_actor_criterion)
                if not filtered_list:
                    print("Nema pronađenih filmova.")
                else:
                    display_controller.display_filtered_movies(filtered_list)

        elif choice == "6":
            movie_country = input("Unesite ime drzave: ")
            if movie_country == "-1":
                continue
            elif movie_country.strip() == "":
                print("Niste uneli drzavu.")
                continue
            elif not validation_controller.movie_valid_country_name(movie_country):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                movie_country_criterion = MovieCriterion(country_of_origin=movie_country)
                filtered_list = movie_controller.search(movie_country_criterion)
                if not filtered_list:
                    print("Nema pronađenih filmova.")
                else:
                    display_controller.display_filtered_movies(filtered_list)

        elif choice == "7":
            movie_year = input("Unesite godinu: ")
            if movie_year == "-1":
                continue
            elif movie_year.strip() == "":
                print("Niste uneli godinu.")
                continue
            elif not validation_controller.movie_valid_year(movie_year):
                print("Nevažeća godina. Molimo pokušajte ponovo.")
                continue
            else:
                movie_year_criterion = MovieCriterion(release_year=movie_year)
                filtered_list = movie_controller.search(movie_year_criterion)
                if not filtered_list:
                    print("Nema pronađenih filmova.")
                else:
                    display_controller.display_filtered_movies(filtered_list)


def search_movie_projection_terms():
    print("PRETRAGA TERMINA BIOSKOPSKIH PROJEKCIJA")
    print("_______________________________________")
    criteria = MovieProjectionTermCriterion()
    while True:
        print("IZBOR KRITERIJUMA")
        print("Za povratak na meni unesite: -1")
        print("1. Naziv filma")
        print("2. Sala")
        print("3. Datum")
        print("4. Vreme početka projekcije")
        print("5. Vreme kraja projekcije")
        print("0. Završi unos kriterijuma")
        choice = input("Unesite broj za kriterijum koji želite da unesete: ")

        if choice == "-1":
            if current_user is None:
                display_menu()
            else:
                display_user_menu()
                return

        if choice == "0":
            break

        elif choice == "1":
            display_controller.display_movies_name()
            print()
            title_choice = input("Unesite ime filma: ")
            if title_choice == "-1":
                continue
            elif not validation_controller.movie_valid_name(title_choice):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.title = title_choice

        elif choice == "2":
            display_controller.display_cinemahall_code()
            hall_code_choice = input("Unesite ID sale: ")
            if hall_code_choice == "-1":
                continue
            elif not 0 < int(hall_code_choice) <= len(cinema_hall_controller.list_of_cinema_halls):
                print("Nevažeći ID. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.hall_code = cinema_hall_controller.list_of_cinema_halls[int(hall_code_choice) - 1].hall_code

        elif choice == "3":
            date_choice = input("Unesite datum projekcije: ")
            if date_choice == "-1":
                continue
            elif not validation_controller.projection_term_valid_date_format(date_choice):
                print("Nevažeći datum. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.date = date_choice

        elif choice == "4":
            start_time_choice = input("Unesite vreme početka projekcije: ")
            if start_time_choice == "-1":
                continue
            elif not validation_controller.projection_valid_time_format(start_time_choice):
                print("Nevažeće vreme. Molimo unesite ponovo.")
                continue
            else:
                criteria.start_time = start_time_choice

        elif choice == "5":
            end_time_choice = input("Unesite vreme kraja projekcije: ")
            if end_time_choice == "-1":
                continue
            elif not validation_controller.projection_valid_time_format(end_time_choice):
                print("Nevažeće vreme. Molimo unesite ponovo.")
                continue
            else:
                criteria.end_time = end_time_choice

        else:
            print("Nevažeći unos. Molimo pokušajte ponovo.")
            continue

    filtered_list = movie_projection_term_controller.search(criteria)
    if not filtered_list:
        print("Nema ponuđenih termina projekcija.")
    else:
        display_controller.display_filtered_projection_term(filtered_list)

    return filtered_list


def search_ticket():
    print("PRETRAGA KARATA")
    print("_______________")
    criteria = TicketCriterion()
    while True:
        print("IZBOR KRITERIJUMA")
        print("Za povratak na meni unesite: -1")
        print("1. Šifra projekcije")
        print("2. Korisnik")
        print("3. Datum")
        print("4. Vreme početka projekcije")
        print("5. Vreme kraja projekcije")
        print("6. Status")
        print("0. Zavrsi unos kriterijuma")

        choice = input("Unesite broj za kriterijum koji zelite da unesete: ")
        if choice == "-1":
            display_user_menu()
            return
        if choice == "0":
            break
        elif choice == "1":
            display_controller.display_projection_codes()
            print()
            code_choice = input("Unesite ID koda projekcije: ")
            if code_choice == "-1":
                continue
            elif not 0 < int(code_choice) <= len(movie_projection_term_controller.list_of_projection_terms):
                print("Nevažeći ID. Molimo pokušajte ponovo.")
                continue
            else:
                criteria.code = movie_projection_term_controller.list_of_projection_terms[
                    int(code_choice) - 1].projection_code

        elif choice == "2":
            user_choice = input("Unesite ime i prezime za neregistrovanog korisnika"
                                " ili username za registrovanog korisnika (username mora da počne sa @):")
            if user_choice == "-1":
                continue
            elif user_choice.startswith('@'):
                user = user_controller.get_user(user_choice[1:])
                if user is None:
                    print("Korisničko ime ne postoji. Molimo pokušajte ponovo.")
                    continue
                else:
                    criteria.owner = user_choice
            else:
                criteria.owner = user_choice

        elif choice == "3":
            date_choice = input("Unesite datum: ")
            if date_choice == "-1":
                continue
            elif not validation_controller.projection_term_valid_date_format(date_choice):
                print("Nevažeći format datuma. Molimo pokušajte ponovo")
                continue
            else:
                criteria.date = date_choice

        elif choice == "4":
            start_time_choice = input("Unesite vreme početka projekcije: ")
            if start_time_choice == "-1":
                continue
            elif not validation_controller.projection_valid_time_format(start_time_choice):
                print("Nevažeće vreme. Molimo unesite ponovo.")
                continue
            else:
                criteria.start_time = start_time_choice
        elif choice == "5":
            end_time_choice = input("Unesite vreme kraja projekcije: ")
            if end_time_choice == "-1":
                continue
            elif not validation_controller.projection_valid_time_format(end_time_choice):
                print("Nevažeće vreme. Molimo unesite ponovo.")
                continue
            else:
                criteria.end_time = end_time_choice

        elif choice == "6":
            print("1. Rezervisana karta")
            print("2. Kupljena karta")
            print()
            status_choice = input("Unesite opciju za status: ")
            if status_choice == "-1":
                continue
            if status_choice == "1":
                criteria.status = 1
            elif status_choice == "2":
                criteria.status = 2
            else:
                print("Nevažeća opcija. Molimo pokušajte ponovo.")
                continue
        else:
            print("Nevažeći unos. Molimo pokušajte ponovo.")
            continue
    filtered_list = ticket_controller.search(criteria)
    if not filtered_list:
        print("Nema pronadjenih karata.")
    else:
        display_controller.display_filtered_ticket(filtered_list)


def reserve_ticket():
    projection_term = None
    seat_choice = None
    reserve_seats = False
    hall = None
    print("REZERVACIJA KARATA")
    print("__________________")
    while True:
        print("ODABIR TERMINA PROJEKCIJE")
        print("_________________________")
        print("1.Pretraga termina projekcije")
        print("2. Direktan unos šifre")
        print("Za povratak na meni unesite: -1")
        choice = input("Unesite broj opcije: ")

        if choice == "-1":
            display_user_menu()

        if choice == "1":
            list_of_projection_terms = search_movie_projection_terms()
            projection_term_choice = int(input("Unesi broj izabrane projekcije: "))
            if projection_term_choice == -1:
                continue
            elif not 0 < projection_term_choice <= len(list_of_projection_terms):
                print("Nevažeći indeks. Molimo pokušajte ponovo.")
            else:
                projection_term = list_of_projection_terms[projection_term_choice - 1]

        if choice == "2":
            display_controller.display_projection_term_codes()
            projection_term_code = input("Unesi ID šifre projekcije: ")
            if projection_term_code == "-1":
                continue
            elif not 0 < int(projection_term_code) <= len(movie_projection_term_controller.list_of_projection_terms):
                print("Nevažeći ID. Molimo pokušajte ponovo.")
                continue
            else:
                projection_term = movie_projection_term_controller.list_of_projection_terms[
                    int(projection_term_code) - 1]

        list_of_tickets = ticket_controller.list_of_tickets
        taken_seats_labels = []
        for ticket in list_of_tickets:
            if ticket.projection_term.code.lower() == projection_term.code.lower():
                taken_seats_labels.append(ticket.seat_label)

        list_of_halls = cinema_hall_controller.list_of_cinema_halls
        for hall_item in list_of_halls:
            if hall_item.hall_code == projection_term.movie_projection.hall.hall_code:
                hall = hall_item

        if not reserve_seats:
            for label in taken_seats_labels:
                row = label[0]
                seat = label[1]
                hall.reserve_seat(row, seat)
                reserve_seats = True

        hall.display_seating_plan()

        seat_choice = input("Unesite oznaku slobodnog sedišta (prvo se unosi broj reda pa oznaka sedista): ")
        if choice == "-1":
            continue
        elif not validation_controller.cinema_hall_valid_seat_label(seat_choice):
            print("Nevažeća oznaka sedišta. Molimo pokušajte ponovo.")
            continue
        else:
            seat_taken = False
            for label in taken_seats_labels:
                if label == seat_choice:
                    seat_taken = True
                    break
            if not seat_taken:
                row = seat_choice[0]
                seat = seat_choice[1]
                if (not (1 <= int(seat_choice[0]) <= int(hall.num_rows)) and
                        seat_choice[1] not in hall.seat_labels_array):
                    print("Sedište ne postoji. Molimo pokušajte kasnije.")
                    continue
                if hall.reserve_seat(row, seat):
                    new_ticket = Ticket(current_user.username, projection_term, seat_choice, 1, None)
                    if ticket_controller.add_ticket(new_ticket):
                        print("Uspešno ste rezervisali kartu.")
                        continue
                    else:
                        print("Rezervacija nije uspela. Molimo pokušajte ponovo.")
                        continue
            else:
                continue


def reserve_tickets_for_salesperson():
    projection_term = None
    seat_choice = None
    reserve_seats = False
    hall = None
    user = None
    print("REZERVACIJA KARATA ZA PRODAVCA")
    print("__________________")
    while True:
        print("Odabir željenog termina projekcije")
        print("1.Pretraga termina projekcije")
        print("2. Direktan unos šifre")
        print("Za povratak na meni unesite: -1")
        choice = input("Unesite broj opcije: ")
        if choice == "-1":
            display_user_menu()

        if choice == "1":
            list_of_projection_terms = search_movie_projection_terms()
            projection_term_choice = int(input("Unesi broj izabrane projekcije: "))
            if projection_term_choice == -1:
                continue
            elif not 0 < projection_term_choice <= len(list_of_projection_terms):
                print("Nevažeći indeks. Molimo pokušajte ponovo.")
                continue
            else:
                projection_term = list_of_projection_terms[projection_term_choice - 1]

        if choice == "2":
            display_controller.display_projection_term_codes()
            projection_term_code = input("Unesi ID šifre projekcije: ")
            if projection_term_code == "-1":
                continue
            elif not 0 < int(projection_term_code) <= len(movie_projection_term_controller.list_of_projection_terms):
                print("Nevažeći ID. Molimo pokušajte ponovo.")
                continue
            else:
                projection_term = movie_projection_term_controller.list_of_projection_terms[
                    int(projection_term_code) - 1]

        name = input("Unesite ime i prezime za neregistrovanog korisnika"
                     " ili username za registrovanog korisnika (username mora da počne sa @): ")
        if name == "-1":
            continue
        elif name.startswith('@'):
            username = user_controller.get_user(name[1:])
            if username is None:
                print("Korisničko ime ne postoji. Molimo pokušajte ponovo.")
                continue
            else:
                user = name[1:]
        else:
            if not validation_controller.ticket_valid_name(name):
                print("Nevažeće ime. Molimo pokušajte kasnije.")
                continue
            else:
                user = name

        list_of_tickets = ticket_controller.list_of_tickets
        taken_seats_labels = []
        for ticket in list_of_tickets:
            if ticket.projection_term.code.lower() == projection_term.code.lower():
                taken_seats_labels.append(ticket.seat_label)

        list_of_halls = cinema_hall_controller.list_of_cinema_halls
        for hall_item in list_of_halls:
            if hall_item.hall_code == projection_term.movie_projection.hall.hall_code:
                hall = hall_item

        if not reserve_seats:
            for label in taken_seats_labels:
                row = label[0]
                seat = label[1]
                hall.reserve_seat(row, seat)
                reserve_seats = True

        hall.display_seating_plan()

        seat_choice = input("Unesite oznaku slobodnog sedista (prvo se unosi broj reda pa oznaka sedista: ")
        if choice == "-1":
            continue
        elif not validation_controller.cinema_hall_valid_seat_label(seat_choice):
            print("Nevažeća oznaka sedišta. Molimo pokušajte ponovo.")
            continue
        else:
            seat_taken = False
            for label in taken_seats_labels:
                if label == seat_choice:
                    seat_taken = True
                    break
            if not seat_taken:
                row = seat_choice[0]
                seat = seat_choice[1]
                if (not (1 <= int(seat_choice[0]) <= int(hall.num_rows)) and
                        seat_choice[1] not in hall.seat_labels_array):
                    print("Sedište ne postoji. Molimo pokušajte kasnije.")
                    continue
                if hall.reserve_seat(row, seat):
                    new_ticket = Ticket(user, projection_term, seat_choice, 1, None)
                    if ticket_controller.add_ticket(new_ticket):
                        print("Uspešno ste rezervisali kartu.")
                        continue
                    else:
                        print("Rezervacija nije uspela. Molimo pokušajte ponovo.")
                        continue
            else:
                continue


def cancellation_of_ticket_reservation():
    print("PONIŠTAVANJE REZERVACIJE KARATA")
    print("_______________________________")
    while True:
        user_reserved_card = display_reserved_tickets_for_user()
        if user_reserved_card is None:
            print("Nema pronađenih rezervisanih karti. Molimo pokušajte ponovo.")
            display_user_menu()
        else:
            print()
            print("Unesite -1 za povratak nazad")
            choice = input("Unesite broj izabrane karte: ")
            if choice == "-1":
                display_user_menu()
                return
            elif not (1 <= int(choice) <= len(user_reserved_card)):
                print("Nevažeći indeks. Molimo pokušajte ponovo.")
                continue
            else:
                ticket = user_reserved_card[int(choice) - 1]
                if ticket_controller.remove_ticket(ticket):
                    print("Uspešno ste poništili rezervaciju karte.")
                    continue
                else:
                    print("Poništavanje rezervacije nije uspelo. Molimo pokušajte ponovo.")
                    continue


def check_and_cancel_reservations():
    current_time = datetime.now()
    tickets_to_remove = []

    for ticket in ticket_controller.list_of_tickets:
        if ticket.status == "1":
            time_until_projection = ticket.projection_term.start_time - current_time
            if time_until_projection < timedelta(minutes=30):
                tickets_to_remove.append(ticket)

    for ticket in tickets_to_remove:
        ticket_controller.remove_ticket(ticket)


def direct_sale_ticket_for_salesperson():
    projection_term = None
    seat_choice = None
    reserve_seats = False
    hall = None
    user = None
    print("DIREKTNA PRODAJA KARTE ZA PRODAVCA")
    print("__________________________________")
    while True:
        print("Odabir željenog termina projekcije")
        print("1.Pretraga termina projekcije")
        print("2. Direktan unos šifre")
        print("Za povratak na meni unesite: -1")
        choice = input("Unesite broj opcije: ")
        if choice == "-1":
            display_user_menu()
        if choice == "1":
            list_of_projection_terms = search_movie_projection_terms()
            projection_term_choice = int(input("Unesi broj izabrane projekcije: "))
            if projection_term_choice == -1:
                continue
            elif not 0 < projection_term_choice <= len(list_of_projection_terms):
                print("Nevažeći indeks. Molimo pokušajte ponovo.")
                continue
            else:
                projection_term = list_of_projection_terms[projection_term_choice - 1]

        if choice == "2":
            display_controller.display_projection_term_codes()
            projection_term_code = input("Unesi ID šifre projekcije: ")
            if projection_term_code == "-1":
                continue
            elif not 0 < int(projection_term_code) <= len(movie_projection_term_controller.list_of_projection_terms):
                print("Nevažeći ID. Molimo pokušajte ponovo.")
                continue
            else:
                projection_term = movie_projection_term_controller.list_of_projection_terms[
                    int(projection_term_code) - 1]

        name = input("Unesite ime i prezime za neregistrovanog korisnika"
                     " ili username za registrovanog korisnika (username mora da počne sa @)")
        if name == "-1":
            continue
        elif name.startswith('@'):
            username = user_controller.get_user(name[1:])
            if username is None:
                print("Korisničko ime ne postoji. Molimo pokušajte ponovo")
                continue
            else:
                user = name[1:]
        else:
            if not Ticket.valid_name(name):
                print("Nevažeće ime. Molimo pokušajte kasnije.")
                continue
            else:
                user = name

        list_of_tickets = ticket_controller.list_of_tickets
        taken_seats_labels = []
        for ticket in list_of_tickets:
            if ticket.projection_term.code.lower() == projection_term.code.lower():
                taken_seats_labels.append(ticket.seat_label)

        list_of_halls = cinema_hall_controller.list_of_cinema_halls
        for hall_item in list_of_halls:
            if hall_item.hall_code == projection_term.movie_projection.hall.hall_code:
                hall = hall_item

        if not reserve_seats:
            for label in taken_seats_labels:
                row = label[0]
                seat = label[1]
                hall.reserve_seat(row, seat)
                reserve_seats = True

        hall.display_seating_plan()

        seat_choice = input("Unesite oznaku slobodnog sedista (prvo se unosi broj reda pa oznaka sedista: ")
        if choice == "-1":
            continue
        elif not validation_controller.cinema_hall_valid_seat_label(seat_choice):
            print("Nevažeća oznaka sedišta. Molimo pokušajte ponovo.")
            continue
        else:
            seat_taken = False
            for label in taken_seats_labels:
                if label == seat_choice:
                    seat_taken = True
                    break
            if not seat_taken:
                row = seat_choice[0]
                seat = seat_choice[1]
                if (not (1 <= int(seat_choice[0]) <= int(hall.num_rows)) and
                        seat_choice[1] not in hall.seat_labels_array):
                    print("Sedište ne postoji. Molimo pokušajte kasnije.")
                    continue
                if hall.reserve_seat(row, seat):
                    new_ticket = Ticket(user, projection_term, seat_choice, 2, None)

                price = float(projection_term.movie_projection.ticket_price)
                projection_date = projection_term.date
                if projection_date.weekday() == 1:
                    price -= 50
                elif projection_date.weekday() in [5, 6]:
                    price += 50
                user_item = user_controller.get_user(name[1:])
                if user_item is not None and user_item.check_eligibility_for_discount():
                    price = price * 0.9
                new_sold_ticket = SoldTicket(current_user.username, new_ticket, price)
                if ticket_controller.add_ticket(new_ticket) and sold_tickets_controller.add_sold_ticket(
                        new_sold_ticket):
                    print("Uspešno ste prodali kartu.")
                else:
                    print("Prodaja nije uspela. Molimo pokušajte ponovo.")
            else:
                continue


def sale_of_reserved_tickets():
    print("PRODAJA REZERVISANE KARTE")
    print("_________________________")
    while True:
        tickets = []
        for ticket in ticket_controller.list_of_tickets:
            if ticket.status == "1":
                tickets.append(ticket)

        display_controller.display_filtered_ticket(tickets)
        print()
        reservation_choice = int(input("Unesi ID izabrane rezervacije: "))
        if reservation_choice == -1:
            continue
        elif not 0 < reservation_choice <= len(tickets):
            print("Nevažeći indeks. Molimo pokušajte ponovo.")
            continue
        else:
            ticket_choice = tickets[reservation_choice - 1]
            projection_date = ticket_choice.projection_term.date
            owner = ticket_choice.owner
            price = float(ticket_choice.projection_term.movie_projection.ticket_price)
            if projection_date.weekday() == 1:
                price -= 50
            elif projection_date.weekday() in [5, 6]:
                price += 50
            user_item = user_controller.get_user(owner)
            if user_item.check_eligibility_for_discount():
                price = price * 0.9
            new_sold_ticket = SoldTicket(current_user.username, ticket_choice, price)
            sold_tickets_controller.add_sold_ticket(new_sold_ticket)
            ticket_controller.sell_ticket(ticket_choice)


def change_ticket_information():
    print("IZMENA KARTE")
    print("____________")
    while True:
        projection_term = None
        owner = None
        seat_label = None
        display_controller.display_projection_term_codes()
        print()
        projection_term_choice = int(input("Unesite ID izabranog termina projekcije: "))
        if projection_term_choice == -1:
            display_user_menu()
            return
        elif not 0 < projection_term_choice <= len(movie_projection_term_controller.list_of_projection_terms):
            print("Nevažeći indeks. Molimo pokušajte ponovo. ")
            continue
        else:
            projection_term = movie_projection_term_controller.list_of_projection_terms[projection_term_choice - 1]

        owner_choice = input("Unesite ime i prezime za neregistrovanog korisnika"
                             " ili username za registrovanog korisnika (username mora da počne sa @)")
        if owner_choice == "-1":
            continue
        elif owner_choice.startswith('@'):
            username = user_controller.get_user(owner_choice[1:])
            if username is None:
                print("Korisničko ime ne postoji. Molimo pokušajte ponovo.")
                continue
            else:
                owner = owner_choice
        else:
            owner = owner_choice

        seat_label_choice = input("Unesite oznaku sedišta: ")
        if seat_label_choice == "-1":
            continue
        elif not validation_controller.cinema_hall_valid_seat_label(seat_label_choice):
            print("Nevažeća oznaka sedišta. Molimo pokušajte ponovo.")
            continue
        else:
            seat_label = seat_label_choice

        current_ticket_copy = Ticket(owner, projection_term, seat_label, 1, None)
        current_ticket = None
        for ticket in ticket_controller.list_of_tickets:
            if (ticket.projection_term.code == current_ticket_copy.projection_term.code and
                    ticket.seat_label == current_ticket_copy.seat_label):
                if current_ticket_copy.owner.startswith('@'):
                    if ticket.owner != current_ticket_copy.owner[1:]:
                        continue
                    else:
                        current_ticket = ticket
                        current_ticket_copy.owner = current_ticket.owner
                else:
                    current_ticket_copy_owner = current_ticket_copy.owner.split()
                    for owner_item in current_ticket_copy_owner:
                        if owner_item not in ticket.owner:
                            continue
                        else:
                            current_ticket = ticket
        if current_ticket is None:
            print("Nema pronađene karte. Molimo pokušajte ponovo.")
        else:
            while True:
                print("IZMENA PODATAKA KARTE")
                print("1. Termin bioskopske projekcije")
                print("2. Korisnik")
                print("3. Sedište")
                print("0. Zavrsi unos kriterijuma")
                choice = input("Unesite broj opcije: ")

                reserve_seats = False
                if choice == "0":
                    break
                if choice == "-1":
                    continue
                elif choice == "1":
                    display_controller.display_projection_term()
                    print()
                    projection_term_choice = int(input("Unesite broj izabranog termina projekcije: "))
                    if projection_term_choice == -1:
                        continue
                    elif not 0 < projection_term_choice <= len(
                            movie_projection_term_controller.list_of_projection_terms):
                        print("Nevažeći indeks. Molimo pokušajte ponovo. ")
                        continue
                    else:
                        check_if_seat_is_taken = False
                        new_ticket = Ticket(None,
                                            movie_projection_term_controller.list_of_projection_terms[
                                                projection_term_choice - 1],
                                            current_ticket.seat_label, 1, None)

                        for ticket in ticket_controller.list_of_tickets:
                            if (ticket.projection_term.code == new_ticket.projection_term.code and
                                    ticket.seat_label == new_ticket.seat_label):
                                check_if_seat_is_taken = True

                        if not check_if_seat_is_taken:
                            current_ticket_copy.owner = current_ticket.owner
                            current_ticket.projection_term = movie_projection_term_controller.list_of_projection_terms[
                                projection_term_choice - 1]
                            update_ticket_in_file(current_ticket_copy, current_ticket)
                        else:
                            print("Sedište u izabranom terminu je već zauzeto.")
                            print("1. Promena sedišta")
                            print("Unesite -1 za povratak nazad")
                            print()
                            choice = input("Unesite opciju: ")
                            if choice == "-1":
                                continue
                            elif choice == "1":
                                list_of_tickets = ticket_controller.list_of_tickets
                                taken_seats_labels = []
                                for ticket in list_of_tickets:
                                    if ticket.projection_term.code.lower() == new_ticket.projection_term.code.lower():
                                        taken_seats_labels.append(ticket.seat_label)

                                list_of_halls = cinema_hall_controller.list_of_cinema_halls
                                for hall_item in list_of_halls:
                                    if hall_item.hall_code == current_ticket.projection_term.movie_projection.hall.hall_code:
                                        hall = hall_item

                                if not reserve_seats:
                                    for label in taken_seats_labels:
                                        row = label[0]
                                        seat = label[1]
                                        hall.reserve_seat(row, seat)

                                hall.display_seating_plan()

                                seat_choice = input(
                                    "Unesite oznaku slobodnog sedista (prvo se unosi broj reda pa oznaka sedista): ")
                                if choice == "-1":
                                    continue
                                elif not validation_controller.cinema_hall_valid_seat_label(seat_choice):
                                    continue
                                else:
                                    seat_taken = False
                                    for label in taken_seats_labels:
                                        if label == seat_choice:
                                            seat_taken = True
                                            break
                                    if not seat_taken:
                                        row = seat_choice[0]
                                        seat = seat_choice[1]
                                        if (not (1 <= int(seat_choice[0]) <= int(hall.num_rows)) and
                                                seat_choice[1] not in hall.seat_labels_array):
                                            print("Sedište ne postoji. Molimo pokušajte kasnije.")
                                            continue
                                        if hall.reserve_seat(row, seat):
                                            current_ticket.seat_label = seat_choice
                                            current_ticket.projection_term = \
                                                movie_projection_term_controller.list_of_projection_terms[
                                                    projection_term_choice - 1]
                                            current_ticket_copy.owner = current_ticket.owner
                                            update_ticket_in_file(current_ticket_copy, current_ticket)
                            else:
                                print("Uneli ste nevažeću opciju. Molimo pokušajte ponovo.")
                                continue
                elif choice == "2":
                    owner_choice = input("Unesite ime i prezime za neregistrovanog korisnika"
                                         " ili username za registrovanog korisnika (username mora da počinje sa @): ")
                    if owner_choice == "-1":
                        continue
                    elif owner_choice.startswith('@'):
                        username = user_controller.get_user(owner_choice[1:])
                        if username is None:
                            print("Korisničko ime ne postoji. Molimo pokušajte ponovo.")
                            continue
                        else:
                            current_ticket.owner = owner_choice[1:]
                            update_ticket_in_file(current_ticket_copy, current_ticket)
                    else:
                        if not validation_controller.user_valid_name(owner_choice):
                            print("Nevažeće ime. Molimo pokušajte kasnije.")
                            continue
                        else:
                            current_ticket.owner = owner_choice
                            update_ticket_in_file(current_ticket_copy, current_ticket)
                elif choice == "3":
                    list_of_tickets = ticket_controller.list_of_tickets
                    taken_seats_labels = []
                    for ticket in list_of_tickets:
                        if ticket.projection_term.code.lower() == current_ticket.projection_term.code.lower():
                            taken_seats_labels.append(ticket.seat_label)

                    list_of_halls = cinema_hall_controller.list_of_cinema_halls
                    for hall_item in list_of_halls:
                        if hall_item.hall_code == current_ticket.projection_term.movie_projection.hall.hall_code:
                            hall = hall_item

                    if not reserve_seats:
                        for label in taken_seats_labels:
                            row = label[0]
                            seat = label[1]
                            hall.reserve_seat(row, seat)

                    hall.display_seating_plan()

                    seat_choice = input(
                        "Unesite oznaku slobodnog sedišta (prvo se unosi broj reda pa oznaka sedišta): ")
                    if choice == "-1":
                        continue
                    elif not validation_controller.cinema_hall_valid_seat_label(seat_choice):
                        continue
                    else:
                        seat_taken = False
                        for label in taken_seats_labels:
                            if label == seat_choice:
                                seat_taken = True
                                break
                        if not seat_taken:
                            row = seat_choice[0]
                            seat = seat_choice[1]
                            if (not (1 <= int(seat_choice[0]) <= int(hall.num_rows)) and
                                    seat_choice[1] not in hall.seat_labels_array):
                                print("Sedište ne postoji. Molimo pokušajte kasnije.")
                                continue
                            if hall.reserve_seat(row, seat):
                                current_ticket.seat_label = seat_choice
                                update_ticket_in_file(current_ticket_copy, current_ticket)
                        else:
                            continue
            update_ticket_in_file(current_ticket_copy, current_ticket)


def cancellation_of_ticket_for_sellperson():
    print("PONIŠTAVNJE REZERVISANIH/PRODATIH KARATA ZA PRODAVCA")
    print("____________________________________________________")
    while True:
        display_controller.display_all_tickets()
        print()
        print("Unesite -1 za povratak nazad")
        choice = input("Unesite broj izabrane karte: ")
        if choice == "-1":
            display_user_menu()
            return
        elif not (1 <= int(choice) <= len(ticket_controller.list_of_tickets)):
            print("Nevažeći indeks. Molimo pokušajte ponovo.")
            continue
        else:
            ticket = ticket_controller.list_of_tickets[int(choice) - 1]
            if ticket_controller.remove_ticket(ticket) and sold_tickets_controller.remove_sold_ticket(ticket):
                print("Uspešno ste poništili rezervaciju karte.")
                continue
            else:
                print()
                print("Poništavanje rezervacije nije uspelo. Molimo pokušajte ponovo.")
                continue


def create_report():
    print("GENERISANJE IZVESTAJA")
    print("_____________________")
    while True:
        print("1. Lista prodatih karata za odabran datum prodaje.")
        print("2. Lista prodatih karata za odabran datum termina bioskopske projekcije.")
        print("3. Lista prodatih karata za odabran datum prodaje i odabranog prodavca.")
        print("4. Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) prodaje.")
        print("5. Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije.")
        print("6. Ukupna cena prodatih karata za zadati film u svim projekcijama.")
        print("7. Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca.")
        print("8. Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakog prodavca) u poslednjih 30 dana.")
        print("9. Ukupan broj i ukupna cena prodatih karata za izabran dan (u prethodnoj nedelji) prodaje.")
        print("10 .Ukupan broj i ukupna cena prodatih karata za izabran dan (u prethodnoj nedelji) održavanja projekcije.")
        choice = input("Unesi broj opcije: ")

        if choice == "-1":
            display_user_menu()
            return

        elif choice == "1":
            date_choice = input("Unesite datum prodaje karte:")
            if date_choice == "-1":
                continue
            elif not validation_controller.projection_term_valid_date_format(date_choice):
                print("Nevažeći format datuma. Molimo pokušajte ponovo. ")
                continue
            else:
                report_controller.sold_tickets_by_sale_date(date_choice)

        elif choice == "2":
            date_choice = input("Unesite datum termina projekcije karte:")
            if date_choice == "-1":
                continue
            elif not validation_controller.projection_term_valid_date_format(date_choice):
                print("Nevažeći format datuma. Molimo pokušajte ponovo. ")
                continue
            else:
                report_controller.sold_tickets_by_projection_term_date(date_choice)

        elif choice == "3":
            date_choice = input("Unesite datum prodaje karte: ")
            if date_choice == "-1":
                continue
            elif not validation_controller.projection_term_valid_date_format(date_choice):
                print("Nevažeći format datuma. Molimo pokušajte ponovo. ")
                continue

            sellperson_choice = input("Unesite korisnicko ime prodavca (treba da počinje sa @):")
            if sellperson_choice == "-1":
                continue
            elif not validation_controller.user_valid_username(sellperson_choice[1:]):
                print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
                continue
            else:
                sellperson = None
                for user in user_controller.list_of_users:
                    if user.username == sellperson_choice[1:] and user.role == "2":
                        sellperson = user
                if sellperson is None:
                    print("Nije pronađen prodavac. Molimo pokušajte kasnije.")
                    continue
                else:
                    report_controller.sold_tickets_by_date_and_sellperson(date_choice, sellperson_choice[1:])

        elif choice == "4":
            print("1. Ponedeljak")
            print("2. Utorak")
            print("3. Sreda")
            print("4. Četvrtak")
            print("5. Petak")
            print("6. Subota")
            print("7. Nedelja")
            day_choice = input("Unesite opciju: ")
            if day_choice == "-1":
                continue
            elif not (1 <= int(day_choice) <= 7):
                print("Nevažeći indeks. Molimo pokušajte ponovo.")
                continue
            else:
                report_controller.sold_tickets_by_sale_day(day_choice)

        elif choice == "5":
            print("1. Ponedeljak")
            print("2. Utorak")
            print("3. Sreda")
            print("4. Četvrtak")
            print("5. Petak")
            print("6. Subota")
            print("7. Nedelja")
            day_choice = input("Unesite opciju: ")
            if day_choice == "-1":
                continue
            elif not (1 <= int(day_choice) <= 7):
                print("Nevažeći indeks. Molimo pokušajte kasnije.")
                continue
            else:
                report_controller.sold_tickets_by_projection_term_day(day_choice)

        elif choice == "6":
            display_controller.display_movies()
            movie_choice = input("Unesitiste ID filma: ")
            if movie_choice == "-1":
                continue
            elif not (1 <= int(movie_choice) <= len(movie_controller.list_of_movies)):
                print("Nevažeći indeks. Molimo pokušajte kasnije.")
                continue
            else:
                report_controller.total_price_for_sold_tickets_by_movie(
                    movie_controller.list_of_movies[int(movie_choice) - 1])

        elif choice == "7":
            print("1. Ponedeljak")
            print("2. Utorak")
            print("3. Sreda")
            print("4. Četvrtak")
            print("5. Petak")
            print("6. Subota")
            print("7. Nedelja")
            day_choice = input("Unesite opciju: ")
            if day_choice == "-1":
                continue
            elif not (1 <= int(day_choice) <= 7):
                print("Nevažeći indeks. Molimo pokušajte kasnije.")
                continue

            sellperson_choice = input("Unesite korisnicko ime prodavca  (treba da počinje sa @):")
            if sellperson_choice == "-1":
                continue
            elif not validation_controller.user_valid_username(sellperson_choice[1:]):
                print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
                continue
            else:
                sellperson = None
                for user in user_controller.list_of_users:
                    if user.username == sellperson_choice[1:] and user.role == "2":
                        sellperson = user
                if sellperson is None:
                    print("Nije pronadjen prodavac. Molimo pokusajte kasnije.")
                    continue
                else:
                    report_controller.sold_tickets_by_sale_day_and_sellperson(day_choice, sellperson_choice)

        elif choice == "8":
            report_controller.sold_tickets_for_each_sellperson_in_last_30_days()

        elif choice == "9":
            print("1. Ponedeljak")
            print("2. Utorak")
            print("3. Sreda")
            print("4. Četvrtak")
            print("5. Petak")
            print("6. Subota")
            print("7. Nedelja")
            day_choice = input("Unesite opciju: ")
            if day_choice == "-1":
                continue
            elif not (1 <= int(day_choice) <= 7):
                print("Nevažeći indeks. Molimo pokušajte ponovo.")
                continue
            else:
                report_controller.sold_tickets_by_sale_day_in_previous_week(day_choice)

        elif choice == "10":
            print("1. Ponedeljak")
            print("2. Utorak")
            print("3. Sreda")
            print("4. Četvrtak")
            print("5. Petak")
            print("6. Subota")
            print("7. Nedelja")
            day_choice = input("Unesite opciju: ")
            if day_choice == "-1":
                continue
            elif not (1 <= int(day_choice) <= 7):
                print("Nevažeći indeks. Molimo pokušajte kasnije.")
                continue
            else:
                report_controller.sold_tickets_by_projection_term_day_in_previous_week(day_choice)



def main():
    while True:
        choice = display_menu()
        if choice == "1":
            registration()
        elif choice == "2":
            login()
        elif choice == "3":
            exit_application()
        elif choice == "4":
            display_available_movies()
        elif choice == "5":
            search_movies()
        elif choice == "6":
            multi_search_movies()
        elif choice == "7":
            search_movie_projection_terms()
        else:
            print("Uneta je neispravna opcija. Molimo pokušajte ponovo.")


if __name__ == '__main__':
    user_controller = UserController()
    user_controller.load_users()

    movie_controller = MovieController()
    movie_controller.load_movies()

    movie_projection_controller = MovieProjectionController()
    movie_projection_controller.load_projections()

    movie_projection_term_controller = MovieProjectionTermController()
    movie_projection_term_controller.load_projection_terms()

    ticket_controller = TicketController()
    ticket_controller.load_tickets()

    cinema_hall_controller = CinemaHallController()
    cinema_hall_controller.load_cinema_halls()

    sold_tickets_controller = SoldTicketController()
    sold_tickets_controller.load_sold_tickets()

    display_controller = DisplayController()

    report_controller = ReportController()

    validation_controller = ValidationController()

    main()
