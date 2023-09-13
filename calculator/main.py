# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("SIMPLE CALCULATOR")


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    return number_1 / number_2


print("""Please select operation :- \n 
1. Add 
2. Subtract 
3. Multiply
4. Divide""")
select = int(input("Select the operation :-"))
num1 = int(input("enter the first number - "))
num2 = int(input("enter the second number - "))
if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input ")
    print("Thank you ")
