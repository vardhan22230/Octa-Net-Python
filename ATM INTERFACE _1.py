class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []
        print("The account is created")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        self.transaction_history.append(Transaction("Deposit", amount))
        print("Deposit successful. Balance in the account is %.2f" % self.balance)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(Transaction("Withdraw", amount))
            print("Withdraw successful. Balance is %.2f" % self.balance)
        else:
            print('Insufficient Balance')

    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.transaction_history.append(Transaction("Transfer to Account", amount))
            target_account.transaction_history.append(Transaction("Transfer from Account", amount))
            print("Transfer successful. Balance is %.2f" % self.balance)
        else:
            print('Insufficient Balance for transfer')

    def print_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction.transaction_type}: {transaction.amount:.2f}")

    def enquiry(self):
        print("Balance in the account is %.2f" % self.balance)

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Enquiry")
            print("5. Print Transaction History")
            print("6. Quit")
            choice = input("Enter your choice (1/2/3/4/5/6): ")
            
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                target_account = acc2  # You can modify this to select a different target account
                amount = float(input("Enter the amount to transfer: "))
                self.transfer(target_account, amount)
            elif choice == '4':
                self.enquiry()
            elif choice == '5':
                self.print_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option (1/2/3/4/5/6).")

# Create two ATM accounts
acc1 = ATM()
acc2 = ATM()

# Display the main menu for the first account
acc1.main_menu()
