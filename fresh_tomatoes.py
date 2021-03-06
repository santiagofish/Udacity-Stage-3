#This file was mostly written by Udacity. I've added the function media_type_determiner, styled the HTML/CSS, and made other (mostly naming--the file was originally set up only for movies) changes in order to assure the page populates correctly, recognizes the three child classes I've set up (Movie, Show, and Book), and  is free of glitches.

import webbrowser  #for launching the static web page in a browser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #EEE;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #CCC;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Favorite Things</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {media_tiles}
    </div>
  </body>
</html>
'''


# A single media entry html template, including additional child-class info.
media_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="200" height="312">
    <h3>{media_title}</h3>
    {media_storyline}
    <br>{media_creator}, {creation_date}
    <br>{child_class_info}
</div>
'''

def media_type_determiner(item):
    '''This function uses the class variable CLASS_NAME to separate each item instance into its appropriate Class, in order to determine which additional data should populate in the item's tile on the web page.
    Input: each item (i.e., instance) in the for loop below
    Output: the particular additional info for each child class'''

    if item.CLASS_NAME == "movie":
        child_class_info = 'Rated ' + item.rating

    elif item.CLASS_NAME == "show":
        child_class_info = 'Season ' + item.season + ', episode ' + item.episode

    elif item.CLASS_NAME == "book":
        child_class_info = item.pages + ' pages'

    return child_class_info

def create_media_tiles_content(favorite_things):
    ''' The HTML content for this section of the page
    Input: favorite_things will be a list of instances
    Output: HTML code for "My Fresh Tomatoes!"'''

    content = ''
    for item in favorite_things:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', item.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', item.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie/show/book with its content filled in
        content += media_tile_content.format(
            media_title = item.title,
            media_storyline = item.storyline,
            poster_image_url = item.poster_image_url,
            trailer_youtube_id = trailer_youtube_id, #from about youtube ID search
            media_creator = 'Created by: ' + item.creator,
            creation_date = item.creation_date,
            child_class_info = media_type_determiner(item)) #procedure to determine relevant additional info for tiles

    return content


def open_media_page(favorite_things):
    '''This procedure brings everything together and launches the page
    Inputs: favorite_things is a list of instances
    Output: populates the provided HTML code and launches 'My Fresh Tomatoes!'''

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the media tiles placeholder with generated content
    rendered_content = main_page_content.format(
        media_tiles = create_media_tiles_content(favorite_things))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
