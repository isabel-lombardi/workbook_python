# Area and Volume
import math

r = int(input("Enter the radius: "))


def area_circle():
    area = (math.pi * (r**2))
    print("The area of a circle with a radius of {} is: {:.3f}".format(r, area))


def volume_sphere():
    volume = math.pi * (4/3 * 6**3)
    print("The volume of a sphere with a radius of {} is: {:.3f}".format(r, volume))


area_circle()
volume_sphere()


