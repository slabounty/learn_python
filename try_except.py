try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err, "Divided by 0")
except ValueError:
    print("Invalid input")
