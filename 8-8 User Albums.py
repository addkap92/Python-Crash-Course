def make_album(name, title, tracks=''):
    album = {'Artist Name': name.title(),
             'Album Title': title.title(),
             }
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print("Please tell me the Artist Name, Album Title and number of tracks if you know. When you're done, enter quit")
    a_name = input("Artist name: ")
    if a_name == 'quit':
        break
    a_title = input("Album Title: ")
    if a_title == 'quit':
        break
    n_tracks = input("Number of tracks: ")
    if n_tracks == 'quit':
        break

    album = make_album(a_name, a_title, n_tracks)
    print(album)