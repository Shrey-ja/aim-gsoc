import math
while True:
    try: #to make sure user enters the values

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("error=> wrong input, try again!!")
        continue
# greatest common divisor

result = math.gcd(num1,num2)

print(f"The GCD of {num1} and {num2} is {result}") #using f string
