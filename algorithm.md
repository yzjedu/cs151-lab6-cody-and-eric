# Algorithm Document

1. Function 1: View
* Name: view
* Parameter: balance
* Return: balance
* Algorithm:
  1. output to the user their current balance
  2. return balance

2. Function 2: Deposit
* Name: deposit
* Parameter: balance
* Return: balance
* Algorithm:
  1. ask user to input the amount they wish to deposit
     1. convert amount to float
  2. while amount <= 0
     1. output to user that the amount is invalid
     2. ask user to input the amount they wish to deposit
        1. convert amount to float
  3. add amount to balance
  4. output to the user their current balance
  5. if balance < 0
     1. output to user that they have a negative balance and will be charged 5% interest
  6. Return balance
  
3. Function 3: Withdraw
* Name: Withdraw
* Parameter: balance
* Return: balance
* Algorithm
  1. ask the user to input the amount they wish to withdraw
     1. convert amount to float
  2. while amount <= 0
     1. output to the user that the amount is invalid
     2. ask the user to input the amount they wish to withdraw
        1. convert amount to a float
  3. subtract the amount from the balance
  4. output to the user their current balance
  5. if balance < 0
     1. output to user that they have a negative balance and will be charged 5% interest
  6. Return balance

4. Function 4: Main Menu
* Name: display_menu
* Parameter: decision
* Return: decision
* Algorithm
  1. output to the user to select an option, deposit, withdraw, view balance, or exit

5. Function 5: Main ATM
* Name: atm
* Parameter: none
* Return: none
* Algorithm
  1. set balance to 1000
  2. output to the user a welcome message
  3. set decision to ""
  4. while decision != 'e'
     1. call display_menu to show decisions to the user
     2. ask user to select their action, D, W, V, or e and convert to lowercase letter
     3. if decision == 'd'
        1. call deposit to get the amount user wishes to deposit
     4. otherwise if decision == 'w'
        1. call withdraw to get amount the user wishes to withdraw
     5. otherwise if decision == 'v'
        1. call view to display the current balance
     6. otherwise if decision == 'e'
        1. output to the user a thank you message
     7. otherwise
        1. output to the user their choice was invalid, and to select a valid one
  5. return balance

6. call atm to start the code