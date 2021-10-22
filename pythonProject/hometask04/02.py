import calendar

def get_full_date(date_str):
    date_arr = date_str.split('/')
    date_arr[1] = calendar.month_name[int(date_arr[1])]
    return " ".join(date_arr)

if __name__ == '__main__':

    date_str = input("enter date in format dd/mm/yyyy: ")
    full_date = get_full_date(date_str)
    print(f"full date: {full_date}")