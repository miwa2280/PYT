from pytest import fixture

from models import BankAccount


@fixture(scope='session')
def bank_account_owner_name() -> str:
    # print(33333333333333333333333333333333333)
    return 'Vasyl'


@fixture()
def deposit_amount_100() -> int:
    # print(222222222222222222222222222222)
    return 100


# @fixture(scope='function')
# @fixture(scope='class')
# @fixture(scope='session')
@fixture(scope='module')
def bank_account(bank_account_owner_name: str) -> BankAccount:
    # print(111111111111111111111111111111111111111)
    bank_account_created = BankAccount(owner=bank_account_owner_name)
    return bank_account_created


@fixture()
def bank_account_2(bank_account_owner_name: str) -> BankAccount:
    # print(444444444444444444444444444)
    bank_account_created = BankAccount(owner=bank_account_owner_name)
    return bank_account_created