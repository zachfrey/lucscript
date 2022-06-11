from re import L
import readsales

def test_readsales():
    sales = readsales.readsales("example.csv");
    assert(sales is not None)
    assert(isinstance(sales, list))


def test_parsesale():
    sale = readsales.parsesale("<example product> <997> <GBP> <example@email> <N> <Ben> <Corey>")
    assert(sale is not None)
    assert(isinstance(sale, dict))
    assert(sale["product"] == "example product")
    assert(sale["price"] is 997)
    assert(sale["currency"] is "GBP")
    assert(sale["email"] is "example@email")
    assert(sale["bonus"] is "N")