from readsales import *
from sales_testdata import *


def test_readsales():
    sales = read_sales("example.csv")
    assert(sales is not None)
    assert(isinstance(sales, list))


def test_parse_sale():
    sale = parse_sale(sale1)
    assert(sale["product"] == "WR")
    assert(sale["price"] == 4056)
    assert(sale["currency"] == "GBP")
    assert(sale["email"] == "joker@gmail.com")
    assert(sale["bonus"] == "E")
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
    assert len(sales_list) == 6
    # TODO: check more content
    assert sales_list[0]["product"] == "WR"
    assert sales_list[0]["seller"][0] == "Ben"
    assert sales_list[0]["seller"][1] == "Corey"

    assert sales_list[4]["email"] == "example@email.uk"

    # sale6 = "<WR full> <4147> <GBP> <N>  <Ashraf_ali_@live.co.uk> <MJR>🚨" 
    assert sales_list[5]["product"] == "WR full"
    assert sales_list[5]["currency"] == "GBP"
    assert sales_list[5]["price"] == 4147
    assert sales_list[5]["email"] == "N"
    assert sales_list[5]["bonus"] == "Ashraf_ali_@live.co.uk"
    assert sales_list[5]["seller"][0] == "MJR"
