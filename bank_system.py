# Full Code: Menu-Driven Bank System in Python
# Step 1: Abstraction & Encapsulation
class Account():
    total_account = 0   # Class variable
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance #encapsulated
        Account.total_account += 1 
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} is credited.")
            print(f"Current Balance: {self.__balance}")
    def withdraw(self,amount):
        if 0< amount < self.__balance:
            self.__balance -= amount 
            print(f"Debited amount: {amount}")
            print(f"Remaining Balance: {self.__balance}")
        else:
            print("Insufficient Balance")
    def get_balance(self):
        return(self.__balance)
    def show_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.__balance}")
    @staticmethod
    def bank_info():
        print("Welcome to ABC Bank- Secure and Simple!")
    @classmethod
    def total_accounts_created(cls):
        print(f"Total accounts created : {cls.total_account}")
# Menu-driven system
accounts = {} # to store multiple accounts
while True:
    print("\n------ MENU ------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show Details")
    print("6. Total Accounts Created")
    print("7. Bank Info")
    print("8. Exit")

    choice = input("Enter the choice (1-8): ")
    if choice == "1":
        name = input("Enter your name: ")
        balance = float(input("Enter initial balance: "))
        acc = Account(name,balance)
        accounts[name] = acc
        print("Account created sucessfully!")
    elif choice == "2":
        name = input("Enter your name: ")
        if name in accounts:
            amount = float(input("Enter the amount: "))
            accounts[name].deposit(amount)
        else:
            print("Account not found")
    elif choice == "3":
        name = input("Enter your name: ")
        if name in accounts:
            amount = float(input("Enter the amount: "))
            accounts[name].withdraw(amount)
        else:
            print("Account not found")
    elif choice == "4":
        name = input("Enter your name: ")
        if name in accounts:
            print(f"Your Balance is: {accounts[name].get_balance()}")
        else:
            print("Account not found.")
    elif choice == '5':
        name = input("Enter name: ")
        if name in accounts:
            accounts[name].show_details()
        else:
            print("Account not found.")
    elif choice == '6':
        Account.total_account_created()
    elif choice == '7':
        Account.bank_info()
    elif choice == '8':
        print("Thank you for using ABC Bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")









