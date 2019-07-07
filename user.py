# practicing oop using basic user class
class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        return self

    def makeDeposit(self, amount):
        self.balance += amount
        return self

    def makeWithdrawal(self, amount):
        self.balance -= amount
        return self

    def displayBalance(self):
        print(self.balance)
        return self

    def transferMoney(self, amount, other):
        if amount > self.balance:
            print('Sorry, not enough funds.')
        else:
            # print(f'Original balance for {other.name} is {other.balance}')
            self.balance -= amount
            other.balance += amount
            # print(f'New balance for {other.name} is {other.balance}')
        return self


mike = user('mike', 500)
ana = user('ana', 500)
john = user('john', 500)


mike.transferMoney(200, ana)