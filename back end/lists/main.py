# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
#1

movies = ["b", "a", "c"]


def alphabetical_order(movies):
    sorted_movies = sorted(movies)
    print(sorted_movies)

alphabetical_order(movies)

#2
# setting list to lower case
golden_glode_wins = [x.lower() for x in ['Jaws', 'Star Wars: Episode IV - A New Hope',
                                         'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']]


def won_golden_globe(movie):
    #setting the string to lower case
    check = movie.lower() in golden_glode_wins
    print(check)


won_golden_globe("Jeff")  # check


#3
toto_albums = {'Fahrenheit', 'The Seventh One', 'Toto XX',
               'Falling in Between', 'Toto XIV', 'Old Is New'}
album_list = ['Fahrenheit', 'The Seventh One', 'Toto XX',
               'Falling in Between', 'Toto XIV', 'Old Is New', 'Smiles', 'Vertigo', 'Two of us']
tidy_list = []

def remove_toto_albums(album_list):
    # Remove all common elements
    tidy_list = [x for x in album_list if x not in toto_albums]
    print(tidy_list)

remove_toto_albums(album_list)

