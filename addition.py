while True:
  try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    break
  except ValueError:
    print("enter the correct value\n")
    continue
# addition
result = num1 + num2

print("The sum of", num1, "and", num2, "is", result)
