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
    assert(sale["price"] == 997)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "example@email")
    assert(sale["bonus"] == "N")
    assert(sale["seller"][0] == "Ben")
    assert(sale["seller"][1] == "Corey")