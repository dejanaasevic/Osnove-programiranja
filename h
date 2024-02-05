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