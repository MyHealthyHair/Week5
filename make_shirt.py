#1
def make_shirt(size, message):
    """size and words"""
    print("\nmake a " + size + " shirt.")
    print('It will say, "' + message + '"')

make_shirt('m', 'xxx')
make_shirt(message="sss", size='m')

#2
def make_shirt(size='large', message='I love Python'):
    """size and words"""
    print("\nmake a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='m')
make_shirt('s', 'ooo')

