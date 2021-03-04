class BankAccount:

    def __init__(self, acc_num, date_of_opening, interest_rate, opening_balance, current_balance):
        self.acc_num = acc_num
        self.date_of_opening = date_of_opening
        self.interest_rate = interest_rate
        self.opening_balance = opening_balance
        self.current_balance = current_balance

    def deposit(self, amount):
        self.current_balance += amount
        return self.current_balance

    def withdraw(self, amount):
        self.current_balance -= amount
        return self.current_balance

    def transfer_money(self, amount):
        pass
