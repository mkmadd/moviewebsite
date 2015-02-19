# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 16:57:17 2015

Modified from exercise in Udacity's Programming Fundamentals with Python class.

Defines the Movie class to encapsulate information about a movie including:
    Rotten Tomatoes id number
    title
    storyline
    poster image url
    trailer Youtube url
    year
    mpaa rating
    critics ratings
    cast
    directors
    synopsis
    Rotten Tomatoes url page
    
The last 7 attributes are designed to be obtained via the Rotten Tomatoes
API, given the Rotten Tomatoes id number for that movie.

For more information on the API, see http://developer.rottentomatoes.com/

@author: Michael K. Maddeford
"""

import webbrowser
import re
import urllib2
import json
import os

class Movie():
    """ This class provides a way to store movie related information. """
    
    def __init__(self, rotten_id, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.rotten_id = rotten_id    # Rotten Tomatoes id to get api info
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        # Extract the unique id from the youtube url and store it
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', trailer_youtube)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', 
                                                         trailer_youtube)
        self.trailer_youtube_id = (youtube_id_match.group(0) 
                                    if youtube_id_match else None)
        
        # Don't get extended info when initializing, don't want to hit api
        # more than 5 times per second
        self._has_extended = False     # did we get extended info already?
        
        # Attributes to be filled in later by call to get_extended_info()
        self.year = None
        self.mpaa_rating = None
        self.critics_ratings = {}
        self.cast = []
        self.directors = []
        self.synopsis = ''
        self.rotten_url = ''
    
    def show_trailer(self):
        """ Open a web browser and play the youtube trailer """
        webbrowser.open(self.trailer_youtube_url)

    def get_extended_info(self):
        """
            Access Rotten Tomatoes api to get extended movie information.
            
            Return None if call was successful, an error otherwise
        """

        # Rotten Tomatoes API url
        rotten_api_url = ('http://api.rottentomatoes.com/api/public/v1.0/movies/'
                          '{movie_id}.json?apikey={api_key}')
        
        # Only need to get this extended information once
        if (self._has_extended):
            return None
            
        # Get json data from Rotten Tomatoes site
        api_key = os.environ['API_KEY']     # Get api key from app.yaml
        url = rotten_api_url.format(movie_id=self.rotten_id, 
                                    api_key=api_key)
        try:
            response = urllib2.urlopen(url)
        except urllib2.URLError, e:
            return e
        
        data = json.load(response)

        # Parse json data into corresponding attributes
        self.year = data['year']
        self.mpaa_rating = data['mpaa_rating']
        self.critics_ratings['critics'] = data['ratings']['critics_score']
        self.critics_ratings['audience'] = data['ratings']['audience_score']
        self.rotten_url = data['links']['alternate']
        self.synopsis = data['synopsis']

        for actor in data['abridged_cast']:
            self.cast.append(actor['name'])
            
        for director in data['abridged_directors']:
            self.directors.append(director['name'])
            
        self._has_extended = True      # Success!

        return None