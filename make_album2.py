def make_album(artist, title, tracks=''):
    """Build a dictionary containing information about an album."""
    album_dict = {'artist': artist.title(),'title': title.title()}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

while True:
    print('\nPlease enter some information: ')
    print("(enter 'q' at any time to quit)")
    
    art = input("Aitists' name:")
    if art == 'q':
        break
        
    tit = input("Titles' name: ")
    if tit == 'q':
        break
        
    name = make_album(art, tit)
    print(name)
