import random

class Bank:
    accounts = []
    
    def __init__(self):
        self.first_name = ''
        self.middle_name = ''
        self.surname = ''
        self.account_number = ''
        self.gender = ''
        self.balance = 0
        self.pin = ''
        
    # Set Pin
    def set_pin(self):
        while True:
            pin = input('Set your pin (Must be 4 digits): ')
            if len(pin) == 4 and pin.isdigit():
                self.pin = pin
                print('Congratulations! Your pin has been set')
                return self.pin
            else:
                print('Your pin should contain 4 digits and numbers only') 
    
    # Open account with the bank
    @classmethod
    def open_account(cls):
        print('Please provide your Personal details to open an account.\n')
        account = Bank()  # Create a new Bank instance for each new account
        account.first_name = input("Enter your first name: ")
        account.middle_name = input("Enter your middle name: ")
        account.surname = input("Enter your surname: ")
        account.gender = input("Male or Female: ")
        account.account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
        account.set_pin()
        cls.accounts.append(account)  # Append the new account to the class-level accounts list
        print(f'Hi {account.first_name}. Account created successfully.\nYour account number is {account.account_number}') 
        
    # Deposit money
    @classmethod
    def deposit(cls):
        acct_no = input("Enter the account number you want to deposit into: ")
        for account in cls.accounts:
            if account.account_number == acct_no:
                try:
                    amount = int(input('How much do you want to deposit? '))
                    if amount > 0:
                        account.balance += amount
                        print(f'Credit alert: ₦{amount:,} deposited into your account.\nBalance: ₦{account.balance:,}')
                    else:
                        print("Amount must be greater than 0")
                except ValueError:
                    print("Please enter a valid amount.")
                return
        print(f'{acct_no} does not exist!')
            
    # Check Balance
    @classmethod
    def check_balance(cls):
        acct_no = input("Enter your account number to check balance: ")
        pin = input('Enter your pin to check account balance: ')
        for account in cls.accounts:
            if account.account_number == acct_no and account.pin == pin:
                print(f'Hi {account.first_name}, Your balance is ₦{account.balance:,}')
                return
        print('Account number or pin is incorrect!')
        
    # Full Account details
    @classmethod
    def details(cls):
        acct_no = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        for account in cls.accounts:
            if account.account_number == acct_no and account.pin == pin:
                print(f'First name: {account.first_name}\nMiddle name: {account.middle_name}\nSurname: {account.surname}\nGender: {account.gender}')
                print(f'Account Number: {account.account_number}\nBalance: ₦{account.balance:,}\n')
                return
        print('Incorrect account number or pin')
        
    # Using the program
    @classmethod
    def open(cls):
        print('Welcome to SWEP bank\n')
        while True:
            print('1. Open Account\n2. Deposit\n3. Check Balance\n4. View account\n5. Close Program')
            try:
                choice = int(input("Choose action: "))
                if choice == 1:
                    cls.open_account()
                elif choice == 2:
                    cls.deposit()
                elif choice == 3:
                    cls.check_balance()
                elif choice == 4:
                    cls.details()
                elif choice == 5:
                    print('Thanks for banking with us.')
                    break
                else:
                    print('Invalid option! Try again')
            except ValueError:
                print("Please enter a valid choice.")

# Run the banking program
Bank.open()

        
        