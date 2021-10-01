#  Сожженные калории. Бег на беговой дорожке позволяет сжигать 4,2 калорий в минуту.
# Напишите программу, которая применяет цикл для вывода количества калорий, сожженных после 10, 15, 20, 25 и 30 минут бега.

def print_qty_calories(calories_per_min, min_range, max_range, step):
    for i in range(min_range, max_range + 1, step):
        print("количество калорий, сожженных после {0} минут = {1}".format(i, i * calories_per_min))

if __name__ == '__main__':
    print_qty_calories(4.2, 10, 30, 5)
