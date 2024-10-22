# Programmers: Cody and Eric
# Course: CS151, Professor Zee
# Due Date: October23th, 2024
# Lab Assignment: Lab 06
# Problem Statement: Build a simulation of an ATM where users can view balance, deposit money, or withdraw money, using functions
# Data In: decision (D, W, V, E), deposit_value (value of deposit), withdraw_value (value of withdraw)
# Data Out: balance (total amount left)
# Credits: none other than class notes

# Function to view balance
def view(balance):
    print("Your current balance is: ", balance)
    return balance


# Function to deposit money
def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    while amount <= 0:
        print('Invalid amount. Try again.')
        amount = float(input("Enter the amount to deposit: "))


    balance += amount
    print("Your current balance is: ", balance)
    if balance < 0:
        print('Warning: You have a negative balance. You will be charged 5% interest.')

    return balance


# Function to withdraw money
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    while amount <= 0:
        print('Invalid amount. Try again.')
        amount = float(input("Enter the amount to withdraw: "))


    balance -= amount
    print("Your current balance is: ", balance)
    if balance < 0:
        print('Warning: You have a negative balance. You will be charged 5% interest.')

    return balance

# Function to display the menu
def display_menu():
    print("\nSelect an option:\nD - Deposit\nW - Withdraw\nV - View Balance\nE - Exit\n")

# Main ATM function
def atm():
    balance = 1000
    print("Welcome to the ATM machine!")

    decision = ""

    while decision != 'e':
        display_menu()
        decision = input("Enter your choice: D, W, V, or E: ").lower()

        if decision == 'd':
            balance = deposit(balance)
        elif decision == 'w':
            balance = withdraw(balance)
        elif decision == 'v':
            balance = view(balance)
        elif decision == 'e':
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Invalid option. Please select a valid choice.")

    return balance

# Start Code
atm()
