from generators.products import generate_dim_product

def test_generate_dim_product_count():
    rows = generate_dim_product(15)
    assert len(rows) == 15

def test_price_range():
    rows = generate_dim_product(30)
    for r in rows:
        assert 5.0 <= r["price"] <= 500.0
