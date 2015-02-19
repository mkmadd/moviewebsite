Project 1, Udacity Full Stack Nanodegree
========================================

The objective of this project was to create a website showing my favorite  
movies, to demonstrate knowledge of Python classes.

The barebones assignment was basically a carbon copy of an exercise done for  
Udacity's Programming Foundations with Python course, and was to use that  
course's fresh_tomatoes.py program to construct this website.

Rather than just construct an html page to sit on my hard drive, I wrote this  
program to run on Google App Engine.  It uses the bottle micro web framework.

Once deployed to Google App Engine, accessing [movie-website.appspot.com](http://movie-website.appspot.com/)  
will display six of my favorite movies, layed out almost identically to the  
webpage constructed by fresh_tomatoes.py.  Clicking on a movie poster image  
will bring up a modal playing that movie's trailer.  Clicking on a movie's  
title will go to a page displaying additional information for that movie,  
selected from Rotten Tomatoes and accessed via their web API.  In addition,  
a link to Rotten Tomatoes webpage for that movie can be found at the bottom  
of the movie page.

Changes were made to the underlying html and css so that:
1) Each movie's title is a hyperlink leading to a separate page displaying  
   more information on that movie, pulled from the Rotten Tomatoes API.

2) Instead of changing the background color of each movie tile on hover over,  
   the image goes opaque and the movie's storyline appears.

   
Structurally, the string variables in the fresh_tomatoes.py file that held  
the html, css, and javascript were broken out into separate files.  The html  
was broken into main, header, movie_tile, and movie templates and moved to a  
views directory.  The css and javascript files were placed in a static  
directory.
