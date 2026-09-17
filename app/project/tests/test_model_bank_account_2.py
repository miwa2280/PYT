from models import BankAccount


class TestBankAccountATMMashineOptimal:
    def test_deposit(self, bank_account: BankAccount, deposit_amount_100: int):
        bank_account.deposit_money(deposit_amount_100)
        bank_account.deposit_money(500)
        assert bank_account.money == 600

    def test_withdraw(self, bank_account: BankAccount):
        bank_account.withdraw_money(100)
        assert bank_account.money == 500

    def test_withdraw_and_deposit(self, bank_account: BankAccount, deposit_amount_100: int):
        bank_account.deposit_money(deposit_amount_100)
        bank_account.withdraw_money(1000)
        assert bank_account.money == -400