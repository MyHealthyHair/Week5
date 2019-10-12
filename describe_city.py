def describe_city(city,country='China'):
    """Describe a city."""
    print('\n' + city.title()+ ' is in '+ country.title() + '.')

describe_city('Shanghai')
describe_city('Tykyo', 'Japan')
describe_city('Beijing')

