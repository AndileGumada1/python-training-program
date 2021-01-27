# Function to check whether a number is a prime number or composite

def prime(n):
    """To check if n is prime or not"""
    x = 1  # this will return 0 if not prime
    for i in range(2, n):
        if n % i == 0:
            x = 0
            break
        else:
            x = 1
        return x


# test if a number is prime or composite
num = int(input("Enter a number: "))


# check if the number is prime or not
result = prime(num)
if result == 1:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

