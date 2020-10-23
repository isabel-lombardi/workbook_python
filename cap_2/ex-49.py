""""" reads a magnitude from the user and displays the appropriate
      descriptor as part of a meaningful message. """

magnitude = float(input("Enter the magnitude: "))

descriptor = ""
if magnitude < 2.0:
    descriptor = "Micro"
elif 2.0 <= magnitude < 3.0:
    descriptor = "Very Minor"
elif 3.0 <= magnitude < 4.0:
    descriptor = "Minor"
elif 4.0 <= magnitude < 5.0:
    descriptor = "Light"
elif 5.0 <= magnitude < 6.0:
    descriptor = "Moderate"
elif 6.0 <= magnitude < 7.0:
    descriptor = "Strong"
elif 7.0 <= magnitude < 8.0:
    descriptor = "Major"
elif 8.0 <= magnitude < 10.0:
    descriptor = "Great"
elif magnitude > 10.0:
    descriptor = "Meteoric"

print("An earthquake of magnitude {} is considered {}".format(magnitude, descriptor))
