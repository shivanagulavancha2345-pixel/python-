def calculator():
	print("Basic Calculator")
	print("Operations: +, -, *, /")

	while True:
		try:
			first_number = float(input("\nEnter the first number: "))
			operator = input("Enter an operation (+, -, *, /): ")
			second_number = float(input("Enter the second number: "))

			if operator == "+":
				result = first_number + second_number
			elif operator == "-":
				result = first_number - second_number
			elif operator == "*":
				result = first_number * second_number
			elif operator == "/":
				if second_number == 0:
					print("Cannot divide by zero.")
					continue
				result = first_number / second_number
			else:
				print("Invalid operation. Please choose +, -, *, or /.")
				continue

			print(f"Result: {result}")

			again = input("Do you want to calculate again? (yes/no): ")
			if again.lower() != "yes":
				print("Goodbye!")
				break

		except ValueError:
			print("Please enter valid numbers.")


calculator()
