import fresh_tomatoes
import media

#Intializing movies with their title and the trailer url to display them on the website

deadpool = media.Movie('deadpool',
                       'https://www.youtube.com/watch?v=ZIM1HydF9UA')

zootopia = media.Movie('zootopia',
                       'https://youtu.be/jWM0ct-OLsM')

avatar = media.Movie('avatar',
                     'https://youtu.be/5PSNL1qE6VY')

hateful_eight = media.Movie('hateful eight',
                            'https://youtu.be/gnRbXn4-Yis')

pulp_fiction = media.Movie('pulp fiction',
                           'https://youtu.be/s7EdQ4FqbhY')

django_unchained = media.Movie('django unchained',
                               'https://youtu.be/eUdM9vrCbow')

#Display the movies on the page
movies = [deadpool, zootopia, avatar, hateful_eight, pulp_fiction,
          django_unchained]
fresh_tomatoes.open_movies_page(movies)


