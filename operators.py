# Equal operator - used to assign values from RHS to LHS operand
num1 = 10
num2 = 20
num3 = num1 + num2
print(num3)

# +=
# ----> num1+= num2
# ----> num1 = num1 + num2

# Data type casting
number = 40
number1 = "25"
print("Data type of number :", type(number))
print("Data type of number1 :", type(number1))
number1 = int(number1) # casting the String to an int
print("Data type of number1 after casting: ", type(number1))

# Using Arithmetic operators

num1 = float(input("Please enter the value of the first number: "))
num1 = float(input("Please enter the value of the second number: "))

# Add the two numbers
add = num1 + num2
print("Sum of the given numbers is : ", add)

# Subtract two numbers
sub = num1 - num2
print("Difference of the two given numbers is: ", sub)

# Multiply two numbers
mult = num1 * num2
print("Product of the two numbers is :", mult)

# Divide two numbers
div = num1 / num2
print("Division of the two given numbers is :", div)

# Modulus of the two numbers
mod = num1 % num2
print("Modulus of the two numbers is :", mod)

# Exponents of the two numbers
expo = num1 ** num2
print("Exponents of the two given numbers is : ", expo)

# Comparison operators
A = 10
B = 15
print("Is A greater than B :", A > B)
print("Is A smaller than B :", A < B)
print("Is A smaller than or equal to Be : ", A <= B)
print("Is A greater than or equal to B :", A >= B)
print("Is A equal to B : ", A == B)
print("Is A not equal to B :", A != B)
