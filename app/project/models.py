import uuid

# Добавляем поддержку uuid7 для Python <= 3.13
if not hasattr(uuid, "uuid7"):
    uuid.uuid7 = uuid.uuid4


class BankAccount:
    def __init__(self, owner: str):
        self.owner = owner
        self.money = 0
        self.id = uuid.uuid7()

    def withdraw_money(self, summa: int) -> None:
        self.money -= summa
        print(
            f"SMS: {self.id} withdraw_money {summa}. Current balance: {self.money}grn"
        )

    def deposit_money(self, summa: int) -> None:
        self.money += summa
        print(
            f"SMS: {self.id} deposit_money {summa}. Current balance: {self.money}grn"
        )