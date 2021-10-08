# 1. Общий объем продаж. Разработайте  программу, которая просит пользователя ввести
# продажи магазина за  каждый день недели.  Суммы должны быть сохранены в  списке.
# Примените цикл, чтобы вычислить общий объем продаж за неделю и показать результат.

import calendar

if __name__ == '__main__':
    sales = [0] * 7
    i = 0
    for day in calendar.day_name:
        sales[i] = int(input("enter sales for {0} ".format(day)))
        i += 1

    total_sales = 0
    for i in sales:
        total_sales += i
    print("Sales sum of the week {0} ".format(total_sales))


