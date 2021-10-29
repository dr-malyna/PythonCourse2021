from pathlib import Path
import matplotlib.pyplot as plt

def get_min(value1, value2):
    if value1 < value2:
        return value1
    return value2

def get_max(value1, value2):
    if value1 > value2:
        return value1
    return value2

def show_plot(y_cords):
    x_cords = []
    for i in range(1,13):
        x_cords.append(i)
    plt.plot(x_cords,y_cords)
    plt.title("Salary fund")
    plt.show()

if __name__ == '__main__':
    min_salary = 0
    max_salary = 0
    sum_salary = 0
    counter = 0
    y_cords = []

    path = 'csv/'
    source_dir = Path(path)
    files = source_dir.glob('*.csv')
    for file in files:
        with file.open('r') as file_dig:
            # print(file_dig.name)
            sum_salary_in_cur_month = 0
            title = file_dig.readline()
            for row in file_dig:
                user_elem = row.split(";")
                if user_elem[0] != "":
                    cur_salary = float(user_elem[len(user_elem) - 1].replace(",", ".").replace(" ", "").replace("в‚ґ", "").rstrip())
                    counter += 1
                    sum_salary += cur_salary
                    sum_salary_in_cur_month += cur_salary
                    if counter == 1:
                        min_salary = cur_salary
                        max_salary = cur_salary
                    else:
                        min_salary = get_min(min_salary, cur_salary)
                        max_salary = get_max(max_salary, cur_salary)
            y_cords.append(sum_salary_in_cur_month)

    print(f"min salary = {min_salary}")
    print(f"max salary = {max_salary}")
    if counter != 0:
        print(f"average salary = {round(sum_salary / counter, 2)}")

    show_plot(y_cords)
