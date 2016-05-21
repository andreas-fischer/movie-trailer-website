import webbrowser
import requests
import json

class Movie(object):
    def __init__(self, title, trailer_youtube_url):

        self.title = title
        self.trailer_youtube_url = trailer_youtube_url

        parsed_json = self.call_api()

        self.poster_image_url = parsed_json['Poster']
        self.storyline = parsed_json['Plot']

    #Call the OMDB API to receive the relevant information about the movie
    def call_api(self):
        r_poster = requests.get('http://www.omdbapi.com/?t=' + self.title + '&y=&plot=full&r=json')
        #If the API returns valid information, parse the JSON file to make the data useable
        if r_poster.status_code == 200:
            parsed_json = json.loads(r_poster.text)
        return parsed_json

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
