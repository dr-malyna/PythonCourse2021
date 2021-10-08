# 3.Разработайте программу, которая позволяет пользователю занести в
# список общее количество дождевых осадков за каждый из  12  месяцев.
# Программа должна вычислить и показать суммарное количество дождевых осадков за
# год,  среднее ежемесячное количество дождевых осадков и месяцы с  самым высоким и
# самым низким количеством дождевых осадков.

import calendar

def get_month_name(index_month):
    return calendar.month_name[index_month + 1]

if __name__ == '__main__':
    precipitation = [0] * 12
    i = 0
    for month_no in range(1,13):
        precipitation[i] = int(input("enter precipitation for {0} ".format(calendar.month_name[month_no])))
        i += 1

    total_precipitations = 0
    for i in precipitation:
        total_precipitations += i
    print("total precipitations {0} ".format(total_precipitations))

    avg_precipitaions = round(total_precipitations / 12, 2)
    print("average precipitaions {0} ".format(avg_precipitaions))

    min_month_of_prcp = precipitation.index(min(precipitation))
    max_month_of_prcp = precipitation.index(max(precipitation))

    print("month with the lowest quantity of precipitation {0} ".format(get_month_name(min_month_of_prcp)))
    print("month with the highest quantity of precipitation {0} ".format(get_month_name(max_month_of_prcp)))
