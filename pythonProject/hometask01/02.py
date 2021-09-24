rectangle_length_1 = int(input("Enter rectangle_length_1: "))
rectangle_width_1 = int(input("Enter rectangle_width_1: "))
rectangle_length_2 = int(input("Enter rectangle_length_2: "))
rectangle_width_2 = int(input("Enter rectangle_width_2: "))

square_1 = rectangle_length_1 * rectangle_width_1
square_2 = rectangle_length_2 * rectangle_width_2
if square_1 < square_2:
    print("second square is bigger than first")
elif square_1 > square_2:
    print("first square is bigger than second")
else:
    print("they are equal")