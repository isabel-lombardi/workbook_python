# Wind Chill

air_temp = float(input("Enter an air temperature: "))
wind_speed = float(input("PEnter the corresponding wind speed: "))

WCI = 13.12 + (0.6215 * air_temp) - (11.37 * (wind_speed ** 0.16)) + (0.3965 * air_temp * (wind_speed ** 0.16))

print("The WCI (Wind Chill Index) is {}.".format(WCI))

