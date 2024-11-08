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
        self.pin = 0
        
    # Set Pin
    def set_pin(self):
        while True:
            pin = input('Set your pin(Must be 4 digits): ')
            if len(pin) == 4 and pin.isdigit():
                self.pin = pin
                print('Congratulations! your pin has been set')
                return self.pin
            else:
                print('Your pin should contain 4 digits and numbers only') 
    
    # Open account with the bank
    def open_account(self):
        print('Please provide your Personal details to open an account.\n')
        self.first_name = input("Enter your first name: ")
        self.middle_name = input("Enter your middle name: ")
        self.surname = input("Enter your Surname: ")
        self.gender = input("Male or Female: ")
        self.account_number = ''.join(str(random.randint(0, 9)) for _ in range(1, 10))
        self.pin = self.set_pin()
        self.accounts.append(self) # appends the account object 
        print(f'Hi {self.first_name}. Account created successfully\nYour account number is {self.account_number}') 
        
    # Deposit money
    def deposit(self):
        acct_no = input("Enter the account number you want to deposit into: ")
        for account in Bank.accounts:
            if account.account_number == acct_no:
                amount = int(input('How much do you want to deposit? '))
                self.balance += amount
                print(f'Credit alert: ₦{amount:,} deposited into your account.\nBalance: ₦{self.balance:,}')
                return
        
        print(f'{acct_no} does not exist!')
            
        
    # Check Balance
    def check_balance(self):
        pin = input('Enter your pin to check account balance: ')
        for pins in Bank.accounts:
            if pins.pin == pin:
                print(f'Hi {self.first_name}, Your balance is ₦{self.balance:,}')
                return
        
        print('Wrong pin!')
        
    # full Account details
    def details(self):
        pin = input("enter your pin: ")
        if pin == self.pin:
            print(f'First name: {self.first_name}\nMiddle name: {self.middle_name}\nSurname: {self.surname}\nGender: {self.gender}')
            print(f'Account Number: {self.account_number}\nBalance: ₦{self.balance:,}\n.')
        else:
            print('Incorrect pin')
        
    # Using the program
    def open(self):
        print('Welcome to SWEP bank\n')
        while True:
            print('1. Open Account\n2. Deposit\n3. Check Balance\n4. View account\n5. Close Program')
            choice = int(input("Choose action: "))
            if choice == 1:
                self.open_account()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.check_balance()
            elif choice == 4:
                self.details()
            elif choice == 5:
                print('Thanks for banking with us.')
                break
            else:
                print('Invalid option! Try again')
    
    
user_1 = Bank()
user_1.open()
        
    
        