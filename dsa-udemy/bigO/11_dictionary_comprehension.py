import random

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

city_temps = {city_name: random.randint(20,30) for city_name in city_names}
print(city_temps)

city_temps_above_25 = {city_name: city_temp for city_name, city_temp in city_temps.items() if city_temp > 25}
print(city_temps_above_25)