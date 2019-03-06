#Make album
def make_album():
    albums = {}
    while True:
        artist = input("Enter a musician: ")
        album = input('Enter an album: ')
        num_tracks = input(album.title() + ' is how many tracks long: ')
        albums[artist] = album
        albums['num_tracks'] = num_tracks
        print (albums)
        return (albums)
        return False

make_album()

