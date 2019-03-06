#Album
def make_album(artist, album, num_tracks):
    albums = {}
    albums[artist] = album
    albums['num_tracks'] = num_tracks
    print (albums)
    return (albums)


make_album('bob', 'experience', 2)
make_album('steve', 'rocks', 34)