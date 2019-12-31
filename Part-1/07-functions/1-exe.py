
# function exercise 

def city_countary(city, countary):
    """City Countary function to format"""

    city_countary_var = f"{city}, {countary}"
    return city_countary_var.title()

india = city_countary('hyderabad', 'india')
print(india)

def make_album( artist_name, album_title, no_songs = None ):


    if no_songs:
        music_album = {
            'artist_name' : artist_name,
            'album_title' : album_title,
            'no_songs'    : no_songs
        }
    else:
        music_album = {
            'artist_name': artist_name,
            'album_title': album_title
        }

    return music_album

album = make_album('s.p.balu', 'hello')
print(album)
album = make_album('s.p.balu', 'hello', 6)
print(album)

def user_make_album(artist_name, album_title, no_songs = None):
    if no_songs:
        music_album = {
            'artist_name': artist_name,
            'album_title': album_title,
            'no_songs': no_songs
        }
    else:
        music_album = {
            'artist_name': artist_name,
            'album_title': album_title
        }

    return music_album

while True:
    print("Please enter the required values: ")
    print("enter q to exit")
    
    a_name = input("Enter artist name: ")
    if a_name == 'q':
        break
    
    a_title = input("enter album title: ")
    if a_title == 'q':
        break
    
    no_songs = input("Enter no of songs: ")
    if no_songs:
        music_album = user_make_album(a_name, a_title, no_songs)
    else:
        music_album = user_make_album(a_name, a_title)

    print(music_album)
