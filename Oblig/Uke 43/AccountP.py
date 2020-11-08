class AccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)

    def transfer(self, amount, receiver):
        self.withdraw(amount)
        receiver.deposit(amount)


def test_deposit():
    test_account = AccountP("Test", "Testesen", 1, 100)
    test_account.deposit(10)
    tol = 10e-14
    success = abs(test_account.get_balance() - 110) < tol
    assert success, 'Deposit failed'


def test_withdraw():
    test_account = AccountP('Testine', "Testesen", 2, 100)
    test_account.withdraw(10)
    tol = 10e-14
    success = abs(test_account.get_balance() - 90) < tol
    assert success, 'Withdrawal failed'


def test_transfer():
    test_account1 = AccountP('Prova', 'Provaccio', 3, 100)
    test_account2 = AccountP('Provo', 'Provaccio', 4, 100)
    test_account1.transfer(10, test_account2)
    tol = 10e-14
    success = abs(test_account1.get_balance() - 90) < tol and abs(test_account2.get_balance() - 110) < tol
    assert success, 'Transfer failed'


def test_get_balance():
    test_account = AccountP('Prueba', 'Pruebación', 5, 100)
    tol = 10e-14
    success = abs(test_account.get_balance() - 100) < tol
    assert success, 'Wrong balance attained'


if __name__ == '__main__':
    test_deposit()
    test_withdraw()
    test_transfer()
    test_get_balance()

"""
Terminal>>python AccountP.py

"""