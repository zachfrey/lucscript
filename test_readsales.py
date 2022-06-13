from re import L
import readsales

def test_readsales():
    sales = readsales.read_sales("example.csv");
    assert(sales is not None)
    assert(isinstance(sales, list))

sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <N> <Ben> <Corey>"
sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <N> <Alex>"
sale4 = "<HU2> <49> <USD> <example@email.com> <N> <Ben>"
sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"

def test_parse_sale():
    sale = readsales.parse_sale(sale1)
    assert(sale["product"] == "WR")
    assert(sale["price"] == 4056)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "joker@gmail.com")
    assert(sale["bonus"] == "N")
    assert(sale["seller"][0] == "Ben")
    assert(sale["seller"][1] == "Corey")

    sale = readsales.parse_sale(sale5)
    assert(sale["product"] == "HU2")
    assert(sale["price"] == 39.8)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "example@email.uk")
    assert(sale["bonus"] == "N")
    assert(sale["seller"][0] == "Alex")
    