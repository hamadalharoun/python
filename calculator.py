first_number = input("Enter the first number:")
second_number = input("Enter the second number:")
Choose_the_operation = input("Choose the operation (+, -, /, *):")

if first_number.isdigit() and second_number.isdigit():
	first_number = int(first_number)
	second_number = int(first_number)
else:
	print("not valid")


if Choose_the_operation == "+":
	print(int(first_number) + int(second_number))
elif Choose_the_operation == "-":
	print(int(first_number) - int(second_number))
elif Choose_the_operation == "/":
	print(int(first_number) / int(second_number))
elif Choose_the_operation == "*":
	print(int(first_number) * int(second_number))	
else:
	print("not valid")