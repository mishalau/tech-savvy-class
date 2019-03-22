weather = {'coord': {'lon': -71.29, 'lat': 42.3}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 277.3, 'pressure': 1028, 'humidity': 35, 'temp_min': 275.93, 'temp_max': 278.71}, 'visibility': 16093, 'wind': {'speed': 5.7, 'deg': 290}, 'clouds': {'all': 75}, 'dt': 1553011505, 'sys': {'type': 1, 'id': 5255, 'message': 0.0094, 'country': 'US', 'sunrise': 1552992638, 'sunset': 1553036120}, 'id': 4954738, 'name': 'Wellesley', 'cod': 200}

print(weather['coord']['lon'])
# print(weather['weather'])
print(weather['main']['temp'] -273.15) #call the key (temp) in dictionaries, which are in between {}
# import pprint
# pprint.pprint(weather)