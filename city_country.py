def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('shanghai', 'china')
print(city)

city = city_country('beijing', 'china')
print(city)

city = city_country('guangzhou', 'china')
print(city)

