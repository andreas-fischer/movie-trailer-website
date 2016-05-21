# movie-trailer-website
This is a project in the full stack frontend developer nanodegree on Udacity. 
This python script displays different information about predefined movies.

All movie information except the movie trailer is pulled through the public 
OMDb API (http://omdbapi.com/). 

Both fresh_tomatoes.html and fresh_tomatoes.py were provided in its current form by Udacity, no changes have been made.

## How to use

The movies have to be preselected. Define the movies you want to display by 
creating new instances in the entertainment_center.py file. Necessary input is 
the movie title and its trailer url.

Example:

<pre><code>
deadpool = media.Movie('deadpool',
                       'https://www.youtube.com/watch?v=ZIM1HydF9UA')
</code></pre>

To execute simply run the entertainment_center.py file.

# List of information provided by OMDb API

This is a list of the parameters that the current implementation theoretically
would allow to be used. Required variables would need to be added accordingly.

* Title
* Year of intial release
* Rating
* Release date
* Runtime
* Genre
* Directors
* Writers
* Actors
* Plot
* Language
* Country
* # of awards and nominations
* Poster image
* Metascore 
* IMDb rating
* IMDb votes
* IMDb ID
* Type

## Used libraries

* webbrowser
* requests
* json
* os
* re

# Possible additions

* Integrating the YouTube API would allow to skip having to submit the trailer
url.
* Expand the user interface to take advantage of the additional information 
provided by OMDb.
* Allow user input through the user interface.

# Authors

Andreas Fischer, 22.05.2016
 