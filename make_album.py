#1
def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {'artist': artist.title(), 'title': title.title()}
    return album_dict

album = make_album('amy', 'aa')
print(album)

album = make_album('betty', 'bb')
print(album)

album = make_album('cimm', 'cc')
print(album)

#2
print('\n')
def make_album(artist, title, tracks=''):
    """Build a dictionary containing information about an album."""
    album_dict = {'artist': artist.title(),'title': title.title()}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('amy', 'aa')
print(album)

album = make_album('gill', 'gg')
print(album)

album = make_album('flora', 'ff', tracks=3)
print(album)
