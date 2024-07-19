import pytest


# تعیین ترتیب تست
@pytest.mark.order1
def test_returns_pet_inventories():
    pytest.main(["test_returns_pet_inventories.py"])

@pytest.mark.order2
def test_order_for_pets():
    pytest.main(["test_order_for_pet.py"])

@pytest.mark.order3
def test_find_purchase_order_by_ID():
    pytest.main(["test_find_purchase _order_by_ID.py"])

@pytest.mark.order4
def test_delete_purchase_order_by_ID():
    pytest.main(["test_delete_purchase _order_by_ID.py"])