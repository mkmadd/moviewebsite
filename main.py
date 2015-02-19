"""
Created on Fri Feb 10 16:21:02 2015

Project 1 for Udacity's Full Stack Nanodegree

This project uses a class, Movie, in the media.py file developed during the
Programming Fundamentals with Python class to generate a web page showing
some of my favorite movies.

This program was developed for deployment on Google App Engine and uses the
Bottle micro web framework.

The web page html, css, and js are based off the fresh_tomatoes.py program 
given in class.  However, the one page file has been broken up into multiple
html templates and css and js files for better design, then modified to suit
my purposes.

@author: Michael K. Maddeford
"""

import bottle     # micro web framework
import media      # Contains the Movie class

# Create six movies that come to mind when asked about my favorites
httyd = media.Movie('770782733',
                    'How to Train Your Dragon',
                    'A story of a boy and his dragon',
                    ('http://ecx.images-amazon.com/images/I/'
                     '51uJGH71GsL._SY355_.jpg'),
                    'https://www.youtube.com/watch?v=oKiYuIsPxYk')

mummy = media.Movie('10585',
                    'The Mummy',
                    'An ancient evil arises; hilarity ensues',
                    ('http://lh3.ggpht.com/-d-0SSihWgLA/T35WDLXsjvI/'
                     'AAAAAAAA09k/Qe_XJRZrLHU/the-mummy-movie-poster'
                     '-1999_thumb%25255B3%25255D.jpg'),
                    'https://www.youtube.com/watch?v=h3ptPtxWJRs')

incredibles = media.Movie('10011',
                          'The Incredibles',
                          ('A family struggles with being super '
                           'in the modern world'),
                          ('http://www.listoid.com/image/78/list_2_78_'
                          '20101119_080416_190.jpg'),
                          'https://www.youtube.com/watch?v=eZbzbC9285I')

great_escape = media.Movie('17025',
                           'The Great Escape',
                           ('The true(ish) story of one of the largest '
                            'POW breakouts in WWII'),
                           ('http://www.rainywolf.com/wp-content/uploads'
                            '/2013/09/poster.jpg'),
                           'https://www.youtube.com/watch?v=xkwmIDx9RwQ')

enchanted = media.Movie('770670631',
                        'Enchanted',
                        ('An animated Disney princess is banished to New '
                         'York City by her wicked step-mother'),
                        ('http://img2.wikia.nocookie.net/__cb20110310014348/'
                         'disney/images/3/38/Enchanted-poster.jpg'),
                        'https://www.youtube.com/watch?v=Zpo7nEc5FHg')

gladiator = media.Movie('13065',
                        'Gladiator',
                        ('A Roman general turned gladiator takes on '
                         'the Emperor who enslaved him'),
                        ('https://www.movieposter.com/posters/archive/'
                         'main/22/A70-11370'),
                        'https://www.youtube.com/watch?v=ol67qo3WhJk')

movies = [httyd, mummy, incredibles, great_escape, enchanted, gladiator]

# The following two functions determine what is returned when each route
# is requested.

# When the route is '/', display all the movies in the movies list using
# the main.tpl template
@bottle.route('/')
@bottle.view('main')
def main():
    return { 'movies' : movies }

# When the route is an integer within the range of the movies list, show the
# page for the corresponding movie using the movie.tpl template
@bottle.route('/<index:int>')
@bottle.view('movie')
def movie(index):
    # Make sure the given route has a vaild index
    if index >= len(movies) or index < 0:
        return 'Index out of range'
    movie = movies[index]               # Get the desired movie
    status = movie.get_extended_info()  # Get extra info from Rotten Tomatoes
    if status:                          # If an error was returned, display it
        return status
    return { 'movie' : movie }          # Else render movie.tpl with movie

# The main app defined as a starting point for google app engine
app = bottle.default_app()