# Reading Files

films_file = open("films.txt", "r")

films = films_file.readlines()

print(films)

for film in films:
    print(film)

films_file.close()