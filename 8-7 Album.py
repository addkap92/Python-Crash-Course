def make_album(name, title, tracks=''):
    album = {'Artist Name': name.title(),
             'Album Title': title.title(),
             }
    if tracks:
        album['tracks'] = tracks
    return album


album = make_album('jake jonah', 'bees')
print(album)
album = make_album('james jameson', 'birds')
print(album)
album = make_album('jared jardeson', 'flies')
print(album)