from commission import *
from readsales import parse_sales_list

import sales_testdata


def test_add_sales():
    sales_list = parse_sales_list(sales_testdata.sales)
    sales = add_sales(sales_list)

    # Ben's sales: 2028 GBP + 49 USD
    assert sales["Ben"]["GBP"] == 2028
    assert sales["Ben"]["USD"] == 49

    # Corey's sales: 2028 GBP
    assert sales["Corey"]["GBP"] == 2028

    # Alex's sales: 39.8 GBP + 5046 USD
    assert sales["Alex"]["GBP"] == 39.8
    assert sales["Alex"]["USD"] == 5046


def test_total_sales():
    sales_list = parse_sales_list(sales_testdata.sales)
    sales = add_sales(sales_list)

    currency_table = sales_testdata.test_currency_table
    
    totals = total_sales(sales, currency_table)
    # Alex's sales: 39.8 GBP + 5046 USD = 5,094.556 USD
    assert totals["Alex"] == 5094.556

    # Ben's sales: 2028 GBP + 49 USD = 2,523.16 USD
    assert totals["Ben"] == 2523.16

    # Corey's sales: 2028 GBP * 1.22 conversion = 2,474.16 USD
    assert totals["Corey"] == 2474.16

def test_sales_commissions():
    test_keys = ["Alex", "Ben", "Corey"]
    test_values = [5000, 6000, 0]
    sales = dict(zip(test_keys, test_values))

    commissions = calculate_commissions(sales, sales_testdata.test_commissions)

    assert commissions["Alex"] == 250.0
    assert commissions["Ben"] == 240.0
    assert commissions["Corey"] == 0.0

def test_sales_commissions2():
    sales_list = parse_sales_list(sales_testdata.sales)

    currency_table = sales_testdata.test_currency_table

    commissions = add_sales2(sales_list, currency_table, bonus_rates)

    # sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <E> <Ben> <Corey>"
    # sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
    # sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <SG> <Alex>"
    # sale4 = "<HU2> <49> <USD> <example@email.com> <N> <Ben>"
    # sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"

    # Alex commission:
    #   = 49 USD * 5% + 4997 USD * 10% + 39.8 GBP (48.556 USD) * 5%
    #   = 504.5778
    assert commissions["Alex"] == 504.5778

    # Ben commission:
    #   = (4056 GBP / 2) * 7% + 49 USD * 5%
    #   = 175.6412
    assert commissions["Ben"] == 175.6412

    # Corey commission:
    #   = (4056 GBP / 2) * 7% 
    #   = 173.1912
    assert commissions["Corey"] == 173.1912
