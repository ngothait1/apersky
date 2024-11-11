def getNumberOnly(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        else:
            print("Invalid input. Please enter numbers only.")