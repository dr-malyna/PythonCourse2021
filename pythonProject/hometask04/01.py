def get_initials(full_name):
    splitted_name = full_name.split(' ')
    initials = []
    for i in splitted_name:
        initials.append(i.lstrip().capitalize()[0])
    return ".".join(initials)

if __name__ == '__main__':

    full_name = input("enter your full name: ").lstrip()
    initials = get_initials(full_name)
    print(f"initials: {initials}")
