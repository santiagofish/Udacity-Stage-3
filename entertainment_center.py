import media
import fresh_tomatoes

raiders = media.Movie("Raiders of the Lost Ark",
                      "Indiana Jones Kicks Nazi Ass",
                      "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
                      "https://www.youtube.com/watch?v=XkkzKHCx154",
                      "Steven Spielberg",
                      "1981",
                      "PG")

empire = media.Movie("Star Wars, Episode V: The Empire Strikes Back",
                     "Hoth, Dagobah, Cloud City: The Best Star Wars Film of All",
                     "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                     "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                     "George Lucas",
                     "1980",
                     "PG")

the_general = media.Movie("The General",
                     "Keaton as Civil War Hero",
                     "https://upload.wikimedia.org/wikipedia/en/5/59/The_General_poster.jpg",
                     "https://www.youtube.com/watch?v=68lvPMCPWog",
                     "Buster Keaton",
                     "1926",
                     "G")

Ugetsu = media.Movie("Ugetsu Monogatari",
                     "A romantic, tragic, humanistic ghost story",
                     "https://upload.wikimedia.org/wikipedia/commons/7/77/Ugetsu_monogatari_poster.jpg",
                     "https://www.youtube.com/watch?v=ecTMsz_KDIE",
                     "Kenji Mizoguchi",
                     "1953",
                     "N/R")

passion_joan_of_arc = media.Movie("La Passion de Jeanne d'Arc",
                     "Falconetti's is the most powerful film performance ever",
                     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/The_Passion_of_Joan_of_Arc_%281928%29_English_Poster.png/220px-The_Passion_of_Joan_of_Arc_%281928%29_English_Poster.png",
                     "https://www.youtube.com/watch?v=JS4NJt7Z_jo",
                     "Carl Theodor Dreyer",
                     "1928",
                     "N/R")

bottle_rocket = media.Movie("Bottle Rocket",
                     "Wes Anderson's first film, a hilarious buddy heist comedy",
                     "https://upload.wikimedia.org/wikipedia/en/a/ae/Bottle-Rocket.jpg",
                     "https://www.youtube.com/watch?v=hspUSez-rYY",
                     "Wes Anderson",
                     "1996",
                     "R")

grande_illusion = media.Movie("La Grande Illusion",
                     "Jean Renoir's WWI film that foreshadows WWII",
                     "https://upload.wikimedia.org/wikipedia/en/3/33/GrandeIllusion.jpg",
                     "https://www.youtube.com/watch?v=hctrYzVYmfM",
                     "Jean Renoir",
                     "1937",
                     "N/R")

best_of_youth = media.Movie("La Meglio Gioventu",
                     "A six-hour Italian melodrama that is extremely wonderful",
                     "https://upload.wikimedia.org/wikipedia/en/5/5d/BestofYouth.jpg",
                     "https://www.youtube.com/watch?v=eIozQwKTxp0",
                     "Marco Tullio Giordana",
                     "2003",
                     "R")

happy_endings = media.Show("Happy Endings: 'Fowl Play/Date'",
                     "Best episode of a hugely underseen TV show",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Happyendings_s2dvd.png/200px-Happyendings_s2dvd.png",
                     "https://www.youtube.com/watch?v=FH3FUQEwYaE",
                     "David Caspe",
                     "2013",
                     "2",
                     "8")

broad_city = media.Show("Broad City: 'Wisdom Teeth'",
                     "This show is basically the funniest and best love story",
                     "https://upload.wikimedia.org/wikipedia/commons/c/c7/Broad_City_Logo_2014-02-07_20-26.gif",
                     "https://www.youtube.com/watch?v=DhGHu-3asWU",
                     "Abbi Jacobson and Ilana Glazer",
                     "2014",
                     "2",
                     "3")

the_wire = media.Show("The Wire: 'Final Grades'",
                     "Any episode from season 4 is astonishingly good",
                     "https://upload.wikimedia.org/wikipedia/en/a/a3/The_Wire_-_Season_4.jpg",
                     "https://www.youtube.com/watch?v=4JK8j0KNLl0",
                     "David Simon",
                     "2006",
                     "4",
                     "13")

twin_peaks = media.Show("Twin Peaks: 'Lonely Souls'",
                     "Devestating, unforgettable",
                     "https://upload.wikimedia.org/wikipedia/en/e/ea/TwinPeaks_openingshotcredits.jpg",
                     "https://www.youtube.com/watch?v=4QBl-BuEIV8",
                     "David Lynch",
                     "1990",
                     "2",
                     "7")

moby_dick = media.Book("Moby-Dick",
                     "Featuring Ahab, the best, most powerful American literary character",
                     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Moby-Dick_FE_title_page.jpg/800px-Moby-Dick_FE_title_page.jpg",
                     "https://www.youtube.com/watch?v=lZ6NEHDgk58",
                     "Herman Melville",
                     "1851",
                     "378")

rings_of_saturn = media.Book("Rings of Saturn (die Ringe des Saturn)",
                     "Powerful and hard to classify--just read it",
                     "https://upload.wikimedia.org/wikipedia/en/3/3b/TheRingsOfSaturn.jpg",
                     "https://www.youtube.com/watch?v=mcBvnzr1v5k",
                     "W.G. Sebald",
                     "1995",
                     "349")

miss_lonelyhearts = media.Book("La Meglio Gioventu",
                     "A six-hour Italian melodrama that is extremely wonderful",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/West_lonelyhearts.JPG",
                     "https://www.youtube.com/watch?v=eFOS06K4Vro",
                     "Nathanael West",
                     "1933",
                     "208")

the_moth = media.Book("'The Death of the Moth'",
                     "Only a few pages long--read it carefully",
                     "http://www.smith.edu/libraries/libs/rarebook/exhibitions/images/penandpress/large/15c_death_of_moth.jpg",
                     "https://www.youtube.com/watch?v=YTbnOLIl_2M",
                     "Virginia Woolf",
                     "1942",
                     "5")


all_movies = [raiders, empire, the_general, Ugetsu, passion_joan_of_arc, bottle_rocket, grande_illusion, best_of_youth]

all_tv_shows = [happy_endings, broad_city, the_wire, twin_peaks]

all_books = [moby_dick, rings_of_saturn, miss_lonelyhearts, the_moth]

all_media = all_movies + all_tv_shows + all_books

fresh_tomatoes.open_media_page(all_media) # CHECK TO SEE IF CHANGING MOVIES TO MEDIA WORKS
