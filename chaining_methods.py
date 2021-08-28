class User:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0		

    def make_withdrawal(self, amount):
        self.account_balance -= amount	
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount) 

guido = User("Guido van Rossum", "guido@python.com")
Catalan = User("Forca Barca", "FCB@python.com")
BucksFan = User("Deer District", "BUCKS@python.com")

guido.make_withdrawal(100).make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance()
Catalan.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()
BucksFan.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()

# python chaining_methods.py

# echo "# chaining_methods" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/chaining_methods.git
# git push -u origin main