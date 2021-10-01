# Задача номер 14, раздел 5.

def falling_distance(t):
    g = 9.8
    return(round(1 / 2 * g * t ** 2, 2))

if __name__ == '__main__':
    for i in range(1, 11):
        print("Расстояние через {0} секунд = {1}".format(i, falling_distance(i)))
