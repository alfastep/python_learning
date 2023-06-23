from BankAccount import BankAccount


def main():
    name = input("Enter your name: ")
    amount = float(input("Enter balance amount you will be starting with:  "))

    account1 = BankAccount(name, amount)

    while True:
        print()
        print(f"Hello {account1.name}")
        print()
        print("Welcome to the Main Menu, what would you like to do today?")
        print(f"1. Check account balance")
        print(f"2. Make a withdrawal")
        print(f"3. Make a deposit")
        print(f"0. Exit")
        print()

        try:
            choice = input("Enter choice: ")
            print()

            if int(choice) == 1:
                print(account1.display_balance())
            elif int(choice) == 2:
                withdrawal = float(input("How much would you like to withdraw? "))
                account1.withdraw(withdrawal)
                print(account1.display_balance())
            elif int(choice) == 3:
                deposit = float(input("How much wold you like to deposit? "))
                account1.deposit(deposit)
                print(account1.display_balance())
            elif int(choice) == 0:
                return False
            else:
                print("Invalid option chosen. Please choose 0, 1, 2, or 3")
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
