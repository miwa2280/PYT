from cart import ShoppingCart


class TestShoppingCart:

    def test_init_empty_cart(self):
        cart = ShoppingCart()
        assert cart.items == []

    def test_add_new_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 15.0, 3)
        assert len(cart.items) == 1
        assert cart.items[0] == {"name": "Apple", "price": 15.0, "quantity": 3}

    def test_add_existing_item_updates_quantity_and_price(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 15.0, 3)
        cart.add_item("Apple", 18.0, 2)

        assert len(cart.items) == 1
        assert cart.items[0] == {"name": "Apple", "price": 18.0, "quantity": 5}

    def test_remove_existing_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 15.0, 3)
        cart.add_item("Banana", 25.0, 1)

        cart.remove_item("Apple")
        assert len(cart.items) == 1
        assert cart.items[0]["name"] == "Banana"

    def test_remove_non_existing_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 15.0, 3)

        cart.remove_item("Orange")
        assert len(cart.items) == 1

    def test_get_total(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 15.0, 2)
        cart.add_item("Banana", 20.0, 3)

        assert cart.get_total() == 90.0