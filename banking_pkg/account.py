def show_balance(balance):
    print(f"Current balance is:  ${balance}")


def deposit(balance):
    amount = input(f"Enter amount to deposit: ")
    balance += float(amount)
    return balance


def withdraw(balance):
    amount = input(f"Enter amount to withdraw:  ")
    balance -= float(amount)
    return balance


def logout(name):
    print("Thank you " + name, ", you have been logged out")
