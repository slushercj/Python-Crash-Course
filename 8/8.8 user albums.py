def make_album(artist, title, number_of_songs = None):
    return {
        'artist': artist,
        'title': title,
        'number_of_songs': number_of_songs
    }

while True:
    artist = input("Enter the name of the music artist (q to Quit): ")
    if artist == 'q':
        break

    title = input("Enter the album title (q to Quit): ")
    if artist == 'q':
        break

    album = make_album(artist, title)

    print(album)

