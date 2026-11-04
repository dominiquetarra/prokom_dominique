def make_album (artistName, albumTitle) :
    album = {
        'artist': artistName.title(),
        'title': albumTitle.title(),
        }
    return album

album = make_album('lany', 'soft')
print(album)

album = make_album('taylor swift', 'fearless')
print(album)

album = make_album('olivia rodrigo', 'sour')
print(album)

#with the number of songs
def make_album(artistName, albumTitle, num_songs=None):
    album = {
        'artist': artistName.title(),
        'title': albumTitle.title(),
        }
    if num_songs:
        album['num_songs'] = num_songs
    return album

album = make_album('lany', 'a beautiful blur', num_songs=13)
print(album)