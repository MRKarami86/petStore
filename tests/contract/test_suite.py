import pytest


# تعیین ترتیب تست
@pytest.mark.order1
def test_add_pet():
    pytest.main(["test_add_pet.py"])

@pytest.mark.order2
def test_update_pet():
    pytest.main(["test_update_pet.py"])

@pytest.mark.order3
def test_delete_pet():
    pytest.main(["test_delete_pet.py"])