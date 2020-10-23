# Units of time

# Convert seconds in time

s_in_s = 1
m_in_s = 60
h_in_s = (m_in_s * 60)
d_in_s = (h_in_s * 24)

s_user = int(input("Enter the number of seconds: "))

days = s_user // d_in_s
s_user = s_user % d_in_s

hours = s_user // h_in_s
s_user = s_user % h_in_s

minutes = s_user // m_in_s
s_user = s_user % m_in_s

seconds = s_user // s_in_s

print("The equivalent of seconds is:", "%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))
