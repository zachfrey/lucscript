from readsales import *
from sales_testdata import *


def test_readsales():
    sales = read_sales("tests/example.csv")
    assert(sales is not None)
    assert(isinstance(sales, list))


def test_parse_sale():
    sale = parse_sale(sale1, 1)
    assert(sale["line_number"] == 1)
    assert(sale["product"] == "WR")
    assert(sale["price"] == 4056)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "joker@gmail.com")
    assert(sale["seller"][0]["name"] == "Ben")
    assert(sale["seller"][0]["bonus"] == "E")
    assert(sale["seller"][1]["name"] == "Corey")
    assert(sale["seller"][1]["bonus"] == "E")

    sale = parse_sale(sale5, 5)
    assert(sale["line_number"] == 5)
    assert(sale["product"] == "HU")
    assert(sale["price"] == 39.8)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "example@email.uk")
    assert(sale["seller"][0]["bonus"] == "N")
    assert(sale["seller"][0]["name"] == "Alex")


def test_parse_sales_list():
    sales_list = parse_sales_list(sales, 3)
    assert len(sales_list) == 6
    # TODO: check more content
    assert sales_list[0]["product"] == "WR"
    assert sales_list[0]["seller"][0]["name"] == "Ben"
    assert sales_list[0]["seller"][1]["name"] == "Corey"

    assert sales_list[4]["email"] == "example@email.uk"

    # sale6 = "<WR full> <4147> <GBP> <N>  <foobar@live.co.uk> <MJR>🚨"
    assert sales_list[5]["product"] == "WR full"
    assert sales_list[5]["currency"] == "GBP"
    assert sales_list[5]["price"] == 4147
    assert sales_list[5]["email"] == "N"
    assert sales_list[5]["seller"][0]["bonus"] == "foobar@live.co.uk"
    assert sales_list[5]["seller"][0]["name"] == "MJR"
