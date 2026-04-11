import pytest
from product import Product

@pytest.fixture
def sample_product():
    return Product("Laptop", 1000.0, 10)
@pytest.mark.parametrize("amount,expected", [
    (5, 15),
    (0, 10),
    (2, 12),
])
def test_add_stock(sample_product, amount, expected):
    sample_product.add_stock(amount)
    assert sample_product.quantity == expected

def test_add_stock_negative(sample_product):
    with pytest.raises(ValueError):
        sample_product.add_stock(-5)
        
def test_remove_stock(sample_product):
    sample_product.remove_stock(3)
    assert sample_product.quantity == 7

def test_remove_stock_too_much(sample_product):
    with pytest.raises(ValueError):
        sample_product.remove_stock(100)
