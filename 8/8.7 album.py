def make_album(artist, title, number_of_songs = None):
    return {
        'artist': artist,
        'title': title,
        'number_of_songs': number_of_songs
    }

album1 = make_album('Michael Jackson', 'Thriller')
album2 = make_album("Warren G", "Regulate")
album3 = make_album("Kats Eye", "Beautiful Chaos", 5)

albums = [album1, album2, album3]

for album in albums:
    message = f"{album['title']} is an album by {album['artist']}. "
    if album['number_of_songs']:
        message += f'It has {album['number_of_songs']} songs.'

    print(message)
