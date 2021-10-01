#Уровень океана. Допустим, что уровень океана в настоящее время повышается примерно на 1,61 мм в год.
# С учетом этого создайте приложение, которое выводит количество
#миллиметров, на которые океан будет подниматься каждый год в течение следующих 25 лет.


def print_rising_of_ocean_level(rising_of_ocean_level_per_year, starting_year, qty_year):
    level = 0
    for i in range(starting_year, starting_year + qty_year + 1):
        level += rising_of_ocean_level_per_year
        print("океан подымется к {0} году на {1} мм".format(i, round(level, 2)))

if __name__ == '__main__':
    print_rising_of_ocean_level(1.61, 2022, 25)
