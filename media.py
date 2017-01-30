# This file creates the parent class Media and three child classes: Movie, Show, and Book. It is the primary data structure for producing the static web page 'My Fresh Tomatoes!'

class Media():
    '''Parent class to Movie, Show, and Book'''

    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date):

        '''Constructor for Media, containing all instance variable that are common to Movie, Show, and Book objects'''

        self.title = media_title
        self.storyline = media_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.creator = media_creator
        self.creation_date = creation_date

class Movie(Media):
    '''Creating child class Movie within module media'''

    CLASS_NAME = "movie" #for classifying in media_type_determiner() in fresh_tomatoes.py
    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date, movie_rating):

        '''Constructor, inherited largely from parent class Media'''

        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date)
        self.rating = movie_rating  #instance variable particular to movies

class Show(Media):
    '''Creating child class Show, which inherits from Media'''

    CLASS_NAME = "show" #for classifying in media_type_determiner() in fresh_tomatoes.py

    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date, show_season, show_episode):

        '''Constructor, inherited largely from parent class Media'''

        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date)
        self.season = show_season  #instance variables particular to tv shows
        self.episode = show_episode

class Book(Media):
    '''Creating child class that inherits from Media'''

    CLASS_NAME = "book"  #for classifying in media_type_determiner() in fresh_tomatoes.py

    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date, number_of_pages):
        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date)
        self.pages = number_of_pages  #instance variable particular to books
