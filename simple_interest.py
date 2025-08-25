while True:
  try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (in percentage (1-100)): "))
    time = float(input("Enter the number of years for the investment: "))
    break
  except ValueError:
    print("enter the correct value\n")
    continue

# Simple Interest Calculation
interest = (principal * rate * time)/100 #correct formula

print(f"The simple interest for an investment of {principal} at, {rate}, % for, {time}, years is:, {interest}")
