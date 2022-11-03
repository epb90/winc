nice_weather = False
going_outside = True if nice_weather else False
print(going_outside)

nice_weather_odds = .7
party_location = 'inside' if nice_weather_odds < .6 else 'in the yard'