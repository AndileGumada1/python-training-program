# conditional expressions - It's a decision making entity supported by Python, which is also referred to as conditional or ternary operator
# membership expressions are used to test membership of an item in a sequence like list or tuple

python = 3.1

if python == 3.0:
    print("Old version")
elif python == 3.2:
    print("Old version")
elif python == 3.3:
    print("Old version")
elif python == 3.7:
    print("Latest version")
else:
    print("Version unknown")

# loop constructs
Digits = [25, 7, 8, 56, 45, 3, 53, 67, 8, 91]
Sum = 0

for values in Digits:
    Sum = Sum + values

print("The Sum of the elements is: ", Sum)

# Use the while loop to find the sum of all the numbers 1 to 100

x = 100
total = 0
a = 1
while a <= x:
    total = total + a
    a = a + 1

# print the sum
print("The sum of the numbers is :", total)
