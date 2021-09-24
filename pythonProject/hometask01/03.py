age = int(input("Enter your_full_age: "))
if age <= 1:
    print("you are a baby")
elif age > 1 and age < 13:
    print("you are a child")
elif age >= 13 and age < 20:
    print("you are a teenager")
else:
    print("you are an adult")