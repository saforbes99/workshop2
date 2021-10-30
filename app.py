from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


balance = 0
print("          === Automated Teller Machine ===          ")
name = input("Enter name to regiser: ")
pin = input("Enter PIN:  ")

print(f" {name} has been regisered with a starting balance of ${balance}")

while True:
    print("LOGIN")
    name_to_validate = input("Enter username: ")
    pin_to_validate = input("Enter PIN:  ")
    if name_to_validate == name and pin_to_validate == pin:
        print(f"Login Successful! :) ")
        break
    else:
        print("Invalid Credentials")

while True:
    atm_menu(name)
    option = input("Choose and option:  ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)

    elif option == "3":
        balance = account.withdraw(balance)

    elif option == "4":
        account.logout(name)

        break
