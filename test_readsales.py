import readsales

def test_readsales():
    sales = readsales.readsales("example.csv");
    assert(sales is not None)
    assert(isinstance(sales, list))