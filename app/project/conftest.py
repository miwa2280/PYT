import pytest
from cart import ShoppingCart


@pytest.fixture
def default_item() -> dict:
    """Фікстура дефолтного товару"""
    return {"name": "Apple", "price": 15.0, "quantity": 3}


@pytest.fixture
def cart_with_default_item(default_item: dict) -> ShoppingCart:
    """Фікстура кошика з одним дефолтним товаром"""
    cart = ShoppingCart()
    cart.add_item(
        name=default_item["name"],
        price=default_item["price"],
        quantity=default_item["quantity"],
    )
    return cart