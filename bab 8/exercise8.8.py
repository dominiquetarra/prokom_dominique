def make_album (artistName, albumTitle) :
    album = {
        'artist': artistName.title(),
        'title': albumTitle.title(),
        }
    return album

while True :
    print("\nPlease enter the album details")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name : ")
    if artist.lower() == 'q' :
        break
    title = input("Album title : ")
    if title.lower() == 'q' :
        break

    album = make_album(artist, title)
    print(album)