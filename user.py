# practicing oop using basic user class
class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def makeDeposit(self, amount):
        self.balance += amount

    def makeWithdrawal(self, amount):
        self.balance -= amount

    def displayBalance(self):
        print(self.balance)

    def transferMoney(self, amount, u):
        if amount > self.balance:
            print('Sorry, not enough funds.')
        else:
            # print(f'Original balance for {u.name} is {u.balance}')
            self.balance -= amount
            u.balance += amount
            # print(f'New balance for {u.name} is {u.balance}')

mike = user('mike', 500)
ana = user('ana', 500)
john = user('john', 500)



mike.makeDeposit(800)
mike.displayBalance()