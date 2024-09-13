# opening and getting variables
print("Hello, This is my final project")
user_name = input("What is your name? ")
print("Hi " + user_name +", nice to meet you")
print("This is a special calculator, I would need two numbers from you")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
print("Thank you for putting in your numbers, " + str(number_1) + " and " + str(number_2))

# checking and saying to the user every number if he even or odd
if number_1 % 2 == 0:
    print("I can see that the first number is even")
else:
    print("I can see that the first number is odd")
if number_2 % 2 == 0:
    print("And the second is even")
else:
    print("And the second is odd") 

# summary the even or odd 
if number_1 % 2 == 0 and number_2 % 2 == 0:
    print("So both of them are even")
elif number_1 % 2 != 0 and number_2 % 2 != 0:
    print("So both are odd")
else:
    print("So one of them is even, and one is odd")

# the user select what to do
operator = input("please select a operator to run on the numbers: (+, -, *, /) ")   

if operator == "+":
    result = number_1 + number_2
    print(str(number_1) + " + " + str(number_2) + " = " + str(result))
elif operator == "-":
    result = number_1 - number_2
    print(str(number_1) + " - " + str(number_2) + " = " + str(result))
elif operator == "*":
    result = number_1 * number_2
    print(str(number_1) + " * " + str(number_2) + " = " + str(result)) 
elif operator == "/": 
    # going out if the user dont know math rules
    if number_2 == 0:
        print("number_2 is zero, it cant be due math rules as we know them")
    else:
        devision_result = input("You chose division, should the result be integer? (y/n) ")
        if devision_result == "y" or devision_result == "Y":
            result = number_1 // number_2
            print(str(number_1) + " / " + str(number_2) + " = " + str(result))
        elif devision_result == "n" or devision_result == "N":
            result = number_1 / number_2
            print(str(number_1) + " / " + str(number_2) + " = " + str(result))
        else:
            print("Invalid choice! only y or n are allowd!")
else:
    print("Operator " + operator + " is not supported")
    print("An error had occured, please try again")

import time
print(("Thank you " + user_name + " for using the calculator on ") + (time.ctime()))