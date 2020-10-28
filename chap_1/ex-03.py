"""Read the number of containers of each size by the user and show the refund due to him"""
less_containers = 0.10
more_containers = 0.25

less = int(input("Enter the number of containers of one litre or less: "))
more = int(input("Enter the number of containers of more than one litre: "))

refund = (less * less_containers) + (more * more_containers)

print("You will be compensated for ${}".format(refund))
