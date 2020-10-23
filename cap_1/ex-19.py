# Free fall

# How quickly an object is traveling when it hits the ground.

import math


vi = 0   # Initial speed 0m/s
a = 8.9  # Acceleration 9.8/s-2

# Read  the input from the user on metres
d = int(input("Enter the height in metres from which an object is dropped: "))

# Formula
vf = math.sqrt((vi**2) + 2 * a * d)

print("The final speed is: ≈", "%.3f" % vf, "m/s")
