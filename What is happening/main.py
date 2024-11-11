#Yenesis Rabelo What is happening 

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

def create_account():
    account_number = input("Enter account number: ")
    # ensuring the valid numeric balance
    while True:
        try:
            initial_balance = float(input("Enter initial balance: "))
            if initial_balance < 0:
                print("Initial balance cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the initial balance.")
    return BankAccount(account_number, initial_balance)

def get_account(accounts):
    account_number = input("Enter account number: ")
    account = accounts.get(account_number)
    if not account:
        print("Account not found.")
    return account

def main():
    accounts = {}
    
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']:
            account = get_account(accounts)
            if account:
                if choice == '2':
                    while True:
                        try:
                            amount = float(input("Enter deposit amount: "))
                            if amount <= 0:
                                print("Deposit amount must be greater than zero. Try again.")
                            else:
                                if account.deposit(amount):
                                    print(f"Deposited ${amount:.2f} successfully!")
                                else:
                                    print("Invalid deposit amount.")
                                break
                        except ValueError:
                            print("Invalid input. Please enter a valid number for deposit.")
                
                elif choice == '3':
                    while True:
                        try:
                            amount = float(input("Enter withdrawal amount: "))
                            if amount <= 0:
                                print("Withdrawal amount must be greater than zero. Try again.")
                            elif amount > account.get_balance():
                                print("Insufficient funds. Try again.")
                            else:
                                if account.withdraw(amount):
                                    print(f"Withdrawn ${amount:.2f} successfully!")
                                break
                        except ValueError:
                            print("Invalid input. Please enter a valid number for withdrawal.")
                
                elif choice == '4':
                    print(f"Current balance: ${account.get_balance():.2f}")
        
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
