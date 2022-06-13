from re import L
from readsales import *

def test_readsales():
    sales = read_sales("example.csv");
    assert(sales is not None)
    assert(isinstance(sales, list))

sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <N> <Ben> <Corey>"
sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <N> <Alex>"
sale4 = "<HU2> <49> <USD> <example@email.com> <N> <Ben>"
sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"

sales = sale1 + "," + sale2 + "," + sale3 + "," + sale4 + "," + sale5

def test_parse_sale():
    sale = parse_sale(sale1)
    assert(sale["product"] == "WR")
    assert(sale["price"] == 4056)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "joker@gmail.com")
    assert(sale["bonus"] == "N")
    assert(sale["seller"][0] == "Ben")
    assert(sale["seller"][1] == "Corey")

    sale = parse_sale(sale5)
    assert(sale["product"] == "HU2")
    assert(sale["price"] == 39.8)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "example@email.uk")
    assert(sale["bonus"] == "N")
    assert(sale["seller"][0] == "Alex")


def test_parse_sales_list():
    sales_list = parse_sales_list(sales)
    assert len(sales_list) == 5
    # TODO: check content
    assert sales_list[0]["product"] == "WR"
    assert sales_list[4]["email"] == "example@email.uk"