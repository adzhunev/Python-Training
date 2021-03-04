import unittest
from Bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def test_acc_attributes(self):
        self.test_acc = BankAccount(1, '01/03/2021', '3%', 0, 0)
        self.assertEqual(self.test_acc.acc_num, 1)
        self.assertEqual(self.test_acc.date_of_opening, '01/03/2021')
        self.assertEqual(self.test_acc.interest_rate, '3%')
        self.assertEqual(self.test_acc.opening_balance, 0)
        self.assertEqual(self.test_acc.current_balance, 0)

    def test_deposit(self):
        self.test_acc = BankAccount(1, '01/03/2021', '3%', 0, 0)
        result = self.test_acc.deposit(1000)
        self.assertEqual(result, 1000)

    def test_withdraw(self):
        self.test_acc = BankAccount(1, '01/03/2021', '3%', 1000, 1000)
        result = self.test_acc.withdraw(100)
        self.assertEqual(result, 900)

    def test_transfer(self):
        self.test_acc1 = BankAccount(1, '01/03/2021', '3%', 1000, 1000)
        result = self.test_acc1.transfer_money(500)
        self.assertEqual(result, 500)

if __name__ == '__main__':
    unittest.main()
