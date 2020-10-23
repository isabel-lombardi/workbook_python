# Units of time

# Convert seconds in time
s_in_s = 1
m_in_s = 60
h_in_s = (m_in_s * 60)
d_in_s = (h_in_s * 24)

d_user = int(input("Enter the number of days: "))
h_user = int(input("Enter the number of hours: "))
m_user = int(input("Enter the number of minutes: "))
s_user = int(input("Enter the number of seconds: "))

total = (s_user * s_in_s) + (m_user * m_in_s) + (h_user * h_in_s) + (d_user * d_in_s)
print("The total of duration in seconds is: {}".format(total))


