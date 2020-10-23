# Weight of the order of widget and gizmos

widget_gr = 75
gizmos_gr = 112

widget_n = int(input("Enter the number of the widget for the order: "))
gizmos_n = int(input("Enter the number of the gizmos for the order: "))

total_gr = widget_n * widget_gr + gizmos_n * gizmos_gr

print("The total weight for the order is: {} grams".format(total_gr))