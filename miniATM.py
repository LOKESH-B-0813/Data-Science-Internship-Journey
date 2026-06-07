# ATM Machine using Functions

balance = 1000
pin = 1234

# Balance Function
def Bal():
    print("Current Balance:", balance)

# Deposit Function
def Deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit Successful!")
    print("Updated Balance:", balance)

# Withdraw Function
def wd():
    global balance
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful!")
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance!")

# Exit Function
def ext():
    print("Thank you for using ATM!")

# PIN Verification
user_pin = int(input("Enter ATM PIN: "))

if user_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("10. Deposit")
        print("20. Balance")
        print("30. Withdraw")
        print("40. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 10:
            Deposit()

        elif choice == 20:
            Bal()

        elif choice == 30:
            wd()

        elif choice == 40:
            ext()
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN! Access Denied.")
