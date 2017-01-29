import media
import fresh_tomatoes

raiders = media.Movie("Indiana Jones and the Raiders of the Lost Arc",
                      "Indiana Jones Kicks Nazi Ass",
                      "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
                      "https://www.youtube.com/watch?v=XkkzKHCx154")

empire = media.Movie("Star Wars, Episode V: The Empire Strikes Back",
                     "Hoth, Dagoba, Cloud City: The Best Star Wars Film of All",
                     "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                     "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

#empire.show_trailer()

'''the_general = media.Movie()

Ugetsu = media.Movie()

passion_joan_of_arc = media.Movie()

bottle_rocket = media.Movie()'''

all_movies = [raiders, empire]
print media.Movie.__module__

#fresh_tomatoes.open_movies_page(all_movies)
