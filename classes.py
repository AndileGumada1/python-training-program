# A class to handle deposit and withdrawals from a bank

import sys


class Bank(object):
    """Bank related transactions"""


    #
    def __init__(self, name, balance =0.0):
        self.name = name
        self.balance = balance

    # to add thr deposit
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Low Balance , can't withdraw the give amount ")
        else:
            self.balance -= amount
        return self.balance


# Using the Bank class
# Create an account with the given name and balance 0.00
myName = input("Please enter your name :")
b = Bank(myName)

# repeat continuously till choice is 'e' or 'E'
while True:
    print('d -Deposit, w -Withdraw, e -Exit')
    choice = input("Your choice: ")
    if choice == 'e' or choice == 'E':
        sys.exit()

    # amount for deposit or withdraw
    amt = float(input("Enter amount :"))

    # do the transaction
    if choice == 'd' or choice == 'D':
        print("Balance after deposit :", b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print("Balance after withdraw :", b.withdraw(amt))
