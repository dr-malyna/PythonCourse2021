value = int(input("Enter days_of_the_week: "))
if value < 1 or value > 7:
    print("Error: You must enter a number between 1 and 7!")
else:
    if value == 1:
        day = "Monday"
    elif value == 2:
        day = "Tuesday"
    elif value == 3:
        day = "Wednesday"
    elif value == 4:
        day = "Thursday"
    elif value == 5:
        day = "Friday"
    elif value == 6:
        day = "Saturday"
    else:
        day = "Sunday"
    print("Day of the week: {0}".format(day))