from models import BankAccount


class TestBankAccountATMMashine:
    def test_deposit(self):
        bank_account = BankAccount(owner='Vasyl')
        bank_account.deposit_money(100)
        bank_account.deposit_money(200)
        assert bank_account.money == 300

    def test_withdraw(self):
        bank_account = BankAccount(owner='Vasyl')
        bank_account.withdraw_money(100)
        assert bank_account.money == -100

    def test_withdraw_and_deposit(self):
        bank_account = BankAccount(owner='Vasyl')
        bank_account.deposit_money(100)
        bank_account.withdraw_money(100)
        assert bank_account.money == 0
        assert bank_account.money == 0


class TestBankAccountATMMashineOptimal:
    def test_deposit(self, bank_account: BankAccount, deposit_amount_100: int):
        bank_account.deposit_money(deposit_amount_100)
        bank_account.deposit_money(200)
        assert bank_account.money == 300

    def test_withdraw(self, bank_account: BankAccount):
        bank_account.withdraw_money(100)
        assert bank_account.money == 200

    def test_withdraw_and_deposit(self, bank_account: BankAccount, deposit_amount_100: int):
        bank_account.deposit_money(deposit_amount_100)
        bank_account.withdraw_money(100)
        assert bank_account.money == 200


def test_deposit(bank_account: BankAccount, deposit_amount_100: int):
    bank_account.deposit_money(deposit_amount_100)
    bank_account.deposit_money(200)
    assert bank_account.money == 500