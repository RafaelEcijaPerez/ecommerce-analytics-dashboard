from generators.customers import generate_dim_customer
import re

def test_generate_dim_customer_count():
    rows = generate_dim_customer(20)
    assert len(rows) == 20

def test_email_format():
    rows = generate_dim_customer(5)
    pattern = re.compile(r".+@example\.com$")
    for r in rows:
        assert pattern.match(r["email"])
