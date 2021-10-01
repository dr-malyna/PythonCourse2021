# Потеря массы. Если умеренно активный человек будет сокращать свое потребление
# в калориях на 500 калорий в день, то, как правило, он может похудеть примерно на 1,5 кг в месяц.
# Напишите программу, которая позволяет пользователю ввести его исходную массу и затем создает и выводит таблицу,
# показывающую, каким будет его ожидаемая масса в конце каждого месяца в течение следующих 6 месяцев, если он
# останется на этой диете.

def print_diets_weight(starting_weight, change_weight_per_month, qty_months = 6):
    delta_weight = 0
    for i in range(1, qty_months + 1):
        delta_weight += change_weight_per_month
        print("ожидаемая масса к концу {0} месяца = {1} ".format(i, starting_weight - delta_weight))

if __name__ == '__main__':
    starting_weight = float(input("Введите свой начальный вес "))
    print_diets_weight(starting_weight, 1.5)
