# 5. Задача магический квадрат Ло Шу
if __name__ == '__main__':
    def is_that_magic_square(arr):
        sum = []
        for i in range(len(arr)):
            sum_temp = 0
            for j in range(len(arr[i])):
                sum_temp += arr[i][j]
            sum.append(sum_temp)

        for j in range(len(arr)):
            sum_temp = 0
            for i in range(len(arr[i])):
                sum_temp += arr[i][j]
            sum.append(sum_temp)

        sum_temp = 0
        for i in range(len(arr)):
            sum_temp += arr[i][i]
        sum.append(sum_temp)

        sum_temp = 0
        for i in range(len(arr)):
            sum_temp += arr[i][len(arr) - i - 1]
        sum.append(sum_temp)

        return sum.count(sum[0]) == len(sum)

    arr_size = 3
    arr_square = [[0] * arr_size, [0] * arr_size, [0] * arr_size]
    #arr_square = [[4,9,2],[3,5,7],[8,1,6]]

    for i in range(arr_size):
        for j in range(arr_size):
            arr_square[i][j] = int(input(f"enter number for row {i} column {j} "))

    is_magic_arr = is_that_magic_square(arr_square)
    print(f"is that magic square - {is_magic_arr}")