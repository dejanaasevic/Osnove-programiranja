from MovieProjectionTermController import MovieProjectionTermController
from User import User
from Movie import Movie
from UserController import UserController
from MovieController import MovieController
from MovieProjectionController import MovieProjectionController
from MovieCriterion import MovieCriterion
from MovieProjectionTermCriterion import MovieProjectionTermCriterion
from CinemaHall import CinemaHall
from CinemaHallController import CinemaHallController

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
    print("6. Visestruka pretraga filmova")
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
    if choice == "1":
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
        print("2. Izmena licnih podataka")
        print("3. Izlaz iz aplikacije")
        print("4. Pregled dostupnih filmova")
        print("5. Pretraga filmova")
        print("6. Visestruka pretraga filmova")
        print("7. Pretraga termina bioskopskih projekcija")
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
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")


def display_menu_for_registered_salesperson():
    while True:
        print("MENI PRODAVCA")
        print("______________")
        print("Izaberite opciju:")
        print("1. Odjava sa sistema: ")
        print("2. Izmena licnih podataka")
        print("3. Izlaz iz aplikacije")
        print("4. Pregled dostupnih filmova")
        print("5. Pretraga filmova")
        print("6. Visestruka pretraga filmova")
        print("7. Pretraga termina bioskopskih projekcija")
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
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")


def display_menu_for_registered_menager():
    while True:
        print("MENI MENADZERA")
        print("______________")
        print("Izaberi opciju:")
        print("1. Odjava sa sistema: ")
        print("2. Izmena licnih podataka")
        print("3. Izlaz iz aplikacije")
        print("4. Registracija novih prodavaca")
        print("5. Registracija novih menadzera")
        print("6. Pregled dostupnih filmova")
        print("7. Pretraga filmova")
        print("8. Visestruka pretraga filmova")
        print("9. Pretraga termina bioskopskih projekcija")
        choice = input("Unesite broj opcije: ")
        if choice == "1":
            log_out()
        elif choice == "2":
            change_personal_information()
        elif choice == "3":
            exit_application()
        elif choice == "4":
            register_new_sellperson()
        elif choice == "5":
            register_new_menager()
        elif choice == "6":
            display_available_movies()
        elif choice == "7":
            search_movies()
        elif choice == "8":
            multi_search_movies()
        elif choice == "9":
            search_movie_projection_terms()
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")


def login():
    global current_user
    print("PRIJAVA NA SISTEM")
    print("_________________")
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
            print("Pogrešno korisničko ime ili lozinka. Molimo pokušajte ponovo.")


def log_out():
    global current_user
    current_user = None
    print("Uspešno ste se odjavili")
    print()
    main()


def exit_application():
    print("Hvala što ste koristili aplikaciju. Doviđenja!")
    exit()


def change_personal_information():
    global current_user
    while True:
        print("IZMENA LICNIH INFORMACIJA")
        print("_______________________")
        print("Za povratak na meni unesite: -1")
        print("1. Ime")
        print("2. Prezime")
        print("3. Lozinka")
        choice = input("Unesite odgovarajuci broj: ")
        if choice == "-1":
            display_user_menu()
            return

        elif choice == "1":
            new_name = input("Unesite novo ime:")
            if new_name == "-1":
                display_user_menu()
                return
            elif not User.valid_name(new_name):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.name = new_name
                if user_controller.update_user_in_list(current_user):
                    print('Ušepsno ste izmenili ime')
                    current_user.display_user()

        elif choice == "2":
            new_surname = input("Unesite novo prezime:")
            if new_surname == "-1":
                display_user_menu()
                return
            if not User.valid_surname(new_surname):
                print("Nevažeće prezime. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.surname = new_surname
                if user_controller.update_user_in_list(current_user):
                    print('Usepsno ste izmenili prezime')
                    current_user.display_user()
        elif choice == "3":
            new_password = input("Unesite novu lozinku (minimum 6 karaktera sa bar jednom cifrom): ")
            if new_password == "-1":
                display_user_menu()
                return
            if not User.valid_password(new_password):
                print("Nevažeće lozinka. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.password = new_password
                if user_controller.update_user_in_list(current_user):
                    print('Usepsno ste izmenili lozinku')
                    current_user.display_user()
                else:
                    print("Niste uspesno promenili lozinku, molimo probajte ponovo")
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")
    print()


def registration():
    global current_user
    print("REGISTRACIJA NA SISTEM")
    print("_______________________")
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite Vaše korisničko ime: ")
        if username == '-1':
            main()
            return
        elif not User.valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite željenu lozinku: ")
        if password == '-1':
            main()
            return
        elif not User.valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite Vaše ime: ")
        if name == '-1':
            main()
            return
        elif not User.valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite Vaše prezime: ")
        if surname == '-1':
            main()
            return
        elif not User.valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue

        role = 1

        new_user = User(username, password, name, surname, role)
        current_user = new_user
        if user_controller.add_user(new_user):
            print("Uspešno ste se registrovali!!!")
            display_user_menu()
            break
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")
    print()


def register_new_sellperson():
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite korisničko ime: ")
        if username == "-1":
            display_user_menu()
            return
        elif not User.valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite lozinku: ")
        if password == "-1":
            display_user_menu()
            return
        elif not User.valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite ime: ")
        if name == "-1":
            display_user_menu()
            return
        elif not User.valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite prezime: ")
        if surname == "-1":
            display_user_menu()
            return
        elif not User.valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue

        role = 2

        register_new_sellperson = User(username, password, name, surname, role)
        if user_controller.add_user(register_new_sellperson):
            print("Uspesno ste registrovali novog prodavca")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def register_new_menager():
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite korisničko ime: ")
        if username == "-1":
            display_user_menu()
            return
        elif not User.valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite lozinku: ")
        if password == "-1":
            display_user_menu()
            return
        elif not User.valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite ime: ")
        if name == "-1":
            display_user_menu()
            return
        elif not User.valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite prezime: ")
        if surname == "-1":
            display_user_menu()
            return
        elif not User.valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue
        role = 3
        register_new_sellperson = User(username, password, name, surname, role)
        if user_controller.add_user(register_new_sellperson):
            print("Uspesno ste registrovali novog menadzera")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def display_available_movies():
    print("PRIKAZ DOSTUPNIH FILMOVA")
    print("________________________")
    i = 1
    for movie in movie_controller.list_of_movies:
        print(f"FILM {i}")
        movie.display_movie()
        i += 1


def multi_search_movies():
    criteria = MovieCriterion()
    while True:
        print("IZBOR KRITERIJUMA")
        print("1. Naziv")
        print("2. Zanr")
        print("3. Trajanje filma")
        print("4. Reziser")
        print("5. Glavne uloge")
        print("6. Zemlja porekla")
        print("7. Godina proizvodnje")
        print("0. Zavrsi unos kriterijuma")

        choice = input("Unesite broj za kriterijum koji zelite da unesete: ")

        if choice == "0":
            break

        elif choice == "1":
            criteria.title = input("Unesite naziv filma: ")

        elif choice == "2":
            criteria.genre = input("Unesite zanr filma: ")

        elif choice == "3":
            print("1. Maksimalno trajanje")
            print("2. Minimalno trajanje")
            print("3. Opseg trajanja")
            print("4. Tacno trajanje")
            duration_choice = input("Unesite opciju za trajanje filma: ")

            if duration_choice == "1":
                criteria.max_duration = input("Unesite maksimalno trajanje filma: ")
            elif duration_choice == "2":
                criteria.min_duration = input("Unesite minimalno trajanje filma: ")
            elif duration_choice == "3":
                criteria.min_duration = input("Unesite minimalno trajanje filma: ")
                criteria.max_duration = input("Unesite maksimalno trajanje filma: ")
            elif duration_choice == "4":
                criteria.duration = input("Unesite tacno trajanje filma: ")
            else:
                print("Nevažeći unos za trajanje filma.")
        elif choice == "4":
            criteria.director = input("Unesite ime rezisera: ")

        elif choice == "5":
            criteria.main_roles = input("Unesite glavne uloge: ")

        elif choice == "6":
            criteria.country_of_origin = input("Unesite zemlju porekla: ")

        elif choice == "7":
            criteria.release_year = input("Unesite godinu proizvodnje: ")

        else:
            print("Nevažeći unos. Molimo pokušajte ponovo.")

    list = movie_controller.search(criteria)
    display_list(list)


def search_movies():
    print("PRETRAGA FILMOVA")
    print("________________")
    while True:
        print("Za povratak na meni unesite: -1")
        print("1. Naziv")
        print("2. Zanr")
        print("3. Trajanje filma")
        print("4. Reziser")
        print("5. Glavne uloge")
        print("6. Zemlja porekla")
        print("7. Godina proizvodnje")
        choice = input("Izaberite kriterijum po kom zelite da pretrazite filmove: ")
        if choice == "-1":
            display_user_menu()
            return
        elif choice == "1":
            movie_name = input("Unesite naziv filma: ")
            if movie_name == "-1":
                display_user_menu()
                return
            elif not Movie.valid_name(movie_name):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                name_criterion = MovieCriterion(title=movie_name)
                list = movie_controller.search(name_criterion)
                display_list(list)

        elif choice == "2":
            movie_genre = input("Unesite naziv zanra: ")
            if movie_genre == "-1":
                display_user_menu()
                return
            elif not Movie.valid_genre(movie_genre):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                genre_criterion = MovieCriterion(genre=movie_genre)
                list = movie_controller.search(genre_criterion)
                display_list(list)
        elif choice == "3":
            print("Za povratak na meni unesite: -1")
            print("1.Maksimalno trajanje")
            print("2.Minimalno trajanje")
            print("3. Opseg trajanja")
            print("4. Tacno trajanje ")
            choice = input("Izaberi opciju pretrage trajanja filma")
            if choice == '-1':
                continue
            elif choice == '1':
                max_movie_duration = input("Unesite maksimalno trajanje filma u minutima: ")
                if max_movie_duration == '-1':
                    continue
                elif not Movie.valid_duration(max_movie_duration):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    max_movie_duration_criterion = MovieCriterion(max_duration=max_movie_duration)
                    list = movie_controller.search(max_movie_duration_criterion)
                    display_list(list)
            elif choice == '2':
                min_movie_duration = input("Unesite minimalno trajanje filma u minutima: ")
                if min_movie_duration == '-1':
                    continue
                elif not Movie.valid_duration(min_movie_duration):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    min_movie_duration_criterion = MovieCriterion(min_duration=min_movie_duration)
                    list = movie_controller.search(min_movie_duration_criterion)
                    display_list(list)

            elif choice == '3':
                max_movie_duration = input("Unesite maksimalno trajanje filma u minutima: ")
                min_movie_duration = input("Unesite minimalno trajanje filma u minutima: ")
                if max_movie_duration == '-1' or min_movie_duration == '-1':
                    continue
                elif not (Movie.valid_duration(min_movie_duration) or Movie.valid_duration(max_movie_duration)):
                    if int(max_movie_duration) < int(min_movie_duration):
                        print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                        continue
                else:
                    movie_duration_opseg_criterion = MovieCriterion(min_duration=min_movie_duration,
                                                                    max_duration=max_movie_duration)
                    list = movie_controller.search(movie_duration_opseg_criterion)
                    display_list(list)
            elif choice == '4':
                movie_duration = input("Unesite trajanje filma u minutima: ")
                if movie_duration == "-1":
                    display_user_menu()
                    return
                elif not Movie.valid_duration(movie_duration):
                    print("Nevažeće trajanje. Molimo pokušajte ponovo.")
                    continue
                else:
                    movie_duration_criterion = MovieCriterion(duration=movie_duration)
                    list = movie_controller.search(movie_duration_criterion)
                    display_list(list)

        elif choice == "4":
            movie_director = input("Unesite ime rezisera: ")
            if movie_director == "-1":
                display_user_menu()
                return
            elif not Movie.valid_person_name(movie_director):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                movie_director_criterion = MovieCriterion(director=movie_director)
                list = movie_controller.search(movie_director_criterion)
                display_list(list)

        elif choice == "5":
            movie_actor = input("Unesite ime glumca: ")
            if movie_actor == "-1":
                display_user_menu()
                return
            elif not Movie.valid_person_name(movie_actor):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                movie_actor_criterion = MovieCriterion(main_roles=movie_actor)
                list = movie_controller.search(movie_actor_criterion)
                display_list(list)
        elif choice == "6":
            movie_country = input("Unesite ime drzave: ")
            if movie_country == "-1":
                display_user_menu()
                return
            elif not Movie.valid_country_name(movie_country):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                movie_country_criterion = MovieCriterion(country_of_origin=movie_country)
                list = movie_controller.search(movie_country_criterion)
                display_list(list)

        elif choice == "7":
            movie_year = input("Unesite godinu: ")
            if movie_year == "-1":
                display_user_menu()
                return
            elif not Movie.valid_year(movie_year):
                print("Nevažeća godina. Molimo pokušajte ponovo.")
                continue
            else:
                movie_year_criterion = MovieCriterion(release_year=movie_year)
                list = movie_controller.search(movie_year_criterion)
                display_list(list)


def search_movie_projection_terms():
    criteria = MovieProjectionTermCriterion()
    while True:
        print("IZBOR KRITERIJUMA")
        print("1. Naziv filma")
        print("2. Sala")
        print("3. Datum")
        print("4. Vreme pocetka projekcije")
        print("5. Vreme kraja projekcije")
        print("0. Zavrsi unos kriterijuma")

        choice = input("Unesite broj za kriterijum koji zelite da unesete: ")

        if choice == "0":
            break

        elif choice == "1":
            criteria.title = input("Unesite naziv filma: ")

        elif choice == "2":
            criteria.hall_code = input("Unesite oznaku sale: ")

        elif choice == "3":
            criteria.date = input("Unesite datum projekcije: ")

        elif choice == "4":
            criteria.start_time = input("Unesite vreme pocetka projekcije: ")

        elif choice == "5":
            criteria.end_time = input("Unesite vreme kraja projekcije: ")

        else:
            print("Nevažeći unos. Molimo pokušajte ponovo.")

    list = movie_projection_term_controller.search(criteria)
    display_projection_terms_list(list)


def display_list(list):
    if not list:
        print("Nema pronadjenih filmova")
    else:
        i = 1
        for movie in list:
            print(f"FILM {i}")
            movie.display_movie()
            i += 1


def display_projection_terms_list(list):
    if not list:
        print("Nema ponudjenih termina projekcija")
    else:
        i = 1
        for projection_term in list:
            print(f"TERMIN PROJEKCIJE {i}")
            projection_term.display_movie_projection_term()
            i += 1

def display_projection_(list):
    if not list:
        print("Nema ponudjenih termina projekcija")
    else:
        i = 1
        for projection_term in list:
            print(f"PROJEKCIJa {i}")
            projection_term.display_movie_projection()
            i += 1

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


def save_cinema_hall(cinema_hall):
    with open('cinemahalls.txt', 'a') as file:
        file.write(f"{cinema_hall.hall_code}|{cinema_hall.num_rows}|{cinema_hall.seat_labels}|{cinema_hall.hall_name}\n")


def display_projection(a):
    if not a:
        print("Nema ponudjenih termina projekcija")
    else:
        i = 1
        for projection_term in a:
            print(f"PROJEKCIJa {i}")
            projection_term.display_movie_projection()
            i += 1
            print()


if __name__ == '__main__':
    user_controller = UserController()
    user_controller.load_users()
    movie_controller = MovieController()
    movie_controller.load_movies()
    movie_projection_controller = MovieProjectionController()
    movie_projection_controller.load_projections()

    movie_projection_term_controller = MovieProjectionTermController()
    movie_projection_term_controller.load_projection_terms()
    #a = movie_projection_term_controller.list_of_projection_terms
    #display_projection_terms_list(a)
    main()


