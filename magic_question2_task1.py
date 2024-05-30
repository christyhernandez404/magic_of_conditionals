# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

number1 = float(input("Enter first number here: "))
number2 = float(input("Enter second number here: "))
number3 = float(input("Enter third number here: "))

complete_list = [number1, number2,  number3]
largest_number = max(complete_list)
convert_to_int = int(largest_number)

print("The largest number you've entered is", convert_to_int, ".")
