# Units of Pressure

kPa = int(input("Enter the pressure number in kPa: "))

# Convert
pascal = kPa * 1000
psi = pascal / 6895
mmHg = kPa * 7.50062
atm = pascal * 9.86923 * (10 ** -6)

message = "{} equal to: {:.4f} psi, {:.4f} mmHg and {:.4f} atm" .format(kPa, psi, mmHg, atm)
mess_len = len(message)
print("-" * mess_len)
print(message)
print("-" * mess_len)

