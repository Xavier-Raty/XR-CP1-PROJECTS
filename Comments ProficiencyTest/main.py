# Xavier Raty What's Happening?

class BankAccount:  # This is code for a class bank account
    def __init__(self, account_number, balance=0): # The account starts at 0, but you can change the number
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): # This lets you deposit from your account
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): # This allows you to withdraw from your balance
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

def create_account(): # Here, you can create an account 
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main(): # This is the information about your account. This shows everything from/about your account.
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1': # if you select 1, you create an account
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: # if you select 2, 3, or 4, you can make a deposit, withdraw or check your balance.
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        
        elif choice == '5': # if you choose 5, you exit the page.
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.") # If you choice is wrong, you have to try again.

if __name__ == "__main__":
    main()