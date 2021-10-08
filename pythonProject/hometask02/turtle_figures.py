import turtle
from math import sqrt

if __name__ == '__main__':
    a = 120
    b = 80
    while True:
        print('-----------------Menu-------------------')
        print('Вывести на экран одну из фигур')
        print('1. прямоугольник\n2. прямоугольный треугольник\n3. равносторонний треугольник\n4. ромб')
        print('0. Exit')
        answer = int(input("Enter choice: "))
        turtle.clear()
        turtle.home()
        if answer == 0:
            break
        elif answer == 1:
            turtle.forward(a)
            turtle.right(90)
            turtle.forward(b)
            turtle.right(90)
            turtle.forward(a)
            turtle.right(90)
            turtle.forward(b)
        elif answer == 2:
            turtle.right(90)
            turtle.forward(a)
            turtle.left(90)
            turtle.forward(a)
            turtle.left(90 + 45)
            turtle.forward(sqrt(2 * a ** 2))
        elif answer == 3:
            for i in range(3):
                turtle.forward(a)
                turtle.right(90 + 30)
        elif answer == 4:
            turtle.left(50)
            turtle.forward(a)
            turtle.right(100)
            turtle.forward(a)
            turtle.right(180 - 100)
            turtle.forward(a)
            turtle.right(100)
            turtle.forward(a)
        turtle.done
