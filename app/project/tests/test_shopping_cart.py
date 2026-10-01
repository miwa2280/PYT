from cart import ShoppingCart


class TestShoppingCart:

    def test_init_empty_cart(self):
        cart = ShoppingCart()
        assert cart.items == []

    def test_add_new_item(self, default_item: dict):
        cart = ShoppingCart()
        cart.add_item(
            default_item["name"],
            default_item["price"],
            default_item["quantity"],
        )
        assert len(cart.items) == 1
        assert cart.items[0] == default_item

    def test_cart_with_default_item_fixture(
        self, cart_with_default_item: ShoppingCart, default_item: dict
    ):
        assert len(cart_with_default_item.items) == 1
        assert cart_with_default_item.items[0] == default_item

    def test_add_existing_item_updates_quantity_and_price(
        self, cart_with_default_item: ShoppingCart
    ):
        cart_with_default_item.add_item("Apple", 18.0, 2)
        assert len(cart_with_default_item.items) == 1
        assert cart_with_default_item.items[0] == {
            "name": "Apple",
            "price": 18.0,
            "quantity": 5,
        }

    def test_remove_existing_item(self, cart_with_default_item: ShoppingCart):
        cart_with_default_item.remove_item("Apple")
        assert len(cart_with_default_item.items) == 0

    def test_get_total(self, cart_with_default_item: ShoppingCart):
        assert cart_with_default_item.get_total() == 45.0