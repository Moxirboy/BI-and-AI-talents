num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_numbers = num1 + num2
if sum_numbers > 50.8:
    print("The sum is greater than 50.8.")
else:
    print("The sum is not greater than 50.8.")

number = int(input("Enter a number to check if it is between 10 and 20: "))

if 10 <= number <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is not between 10 and 20.")
