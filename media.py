# description here

class Media():  #Parent class to Movie, Show, and Book

    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date):
        self.title = media_title
        self.storyline = media_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.creator = media_creator
        self.creation_date = creation_date

class Movie(Media):
    '''creating child class Movie (within module media)'''

    CLASS_NAME = "movie"

    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date, movie_rating):
        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date)
        self.rating = movie_rating

class Show(Media):
    '''creating child class Show (within module media)'''

    CLASS_NAME = "show"

    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date, show_season, show_episode):
        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date)
        self.season = show_season
        self.episode = show_episode

class Book(Media):
    '''creating child class Book (within module media)'''

    CLASS_NAME = "book"

    def __init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date, number_of_pages):
        Media.__init__(self, media_title, media_storyline, poster_image, trailer_youtube, media_creator, creation_date)
        self.pages = number_of_pages
