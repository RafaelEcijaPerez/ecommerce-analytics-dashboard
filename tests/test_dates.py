from generators.dates import generate_dim_date

def test_generate_dim_date_length():
    rows = generate_dim_date(10)
    assert len(rows) == 10

def test_generate_dim_date_fields():
    row = generate_dim_date(1)[0]
    assert "date_id" in row
    assert "year" in row
    assert "month" in row
    assert "day" in row
    assert "weekday" in row
