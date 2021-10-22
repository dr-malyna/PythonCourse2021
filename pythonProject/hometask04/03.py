def print_recursion_numbers(min_n, max_n):
    if min_n <= max_n:
        print(min_n)
        print_recursion_numbers(min_n + 1, max_n)
    else:
        return

if __name__ == '__main__':
    n = int(input("enter number: "))
    print_recursion_numbers(1,n)