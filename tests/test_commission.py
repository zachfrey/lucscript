from commission import *
from readsales import parse_sales_list, read_sales
import math

import sales_testdata


def test_sales_commissions():
    sales_list = parse_sales_list(sales_testdata.sales, 1)

    currencies = sales_testdata.test_currency_table

    commissions = calculate_commissions(sales_list, currencies, bonus_rates)

    # sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <E> <Ben> <Corey>"
    # sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
    # sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <SG> <Alex>"
    # sale4 = "<HU2> <49> <USD> <example@email.com> <N> <Ben>"
    # sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"

    # Alex commission:
    #   = 49 USD * 50% + 4997 USD * 10% + 39.8 GBP (48.556 USD) * 50%
    #   = 504.5778
    assert math.isclose(commissions["Alex"], 548.478)

    # Ben commission:
    #   = (4056 GBP / 2) * 7% + 49 USD * 50%
    #   = 175.6412
    assert math.isclose(commissions["Ben"], 197.6912)

    # Corey commission:
    #   = (4056 GBP / 2) * 7%
    #   = 173.1912
    assert math.isclose(commissions["Corey"], 173.1912)

    # MJR commission
    # line is bogus (data error) so should be 0
    assert math.isclose(commissions["MJR"], 0.0)


def test_test2_dataset():
    sales = read_sales("tests/Test2-corrected.csv")

    sales_list = []
    line_number = 0
    for line in sales:
        line_number += 1
        sales_list += parse_sales_list(line, line_number)

    currencies = sales_testdata.test_currency_table

    commissions = calculate_commissions(sales_list, currencies, bonus_rates)

    # Start asserting here

    # MJR commission:
    #   = Line with WR commission is bogus, so only HU2 commission
    #   = 28.5
    assert math.isclose(commissions["MJR"], 24.5)

    # Evo commission:
    #   = 3 HU2 commissions = 24.5 * 3
    assert math.isclose(commissions["Evo"], 73.5)

    # Check for bogus sellers
    assert "SG" not in commissions
    assert "E" not in commissions
    assert "N" not in commissions

    # Ahmad commission:
    # = 1334 USDC * 5% = 66.70
    assert math.isclose(commissions["Ahmad"], 66.70)

    # OR commission
    # <WR Final> <5159> <USDC> <Lucdeman@outlook.com> <N> <Ben> <SG> <OR>🚨
    # = 5159 / 2 * 10% = 257.95
    assert math.isclose(commissions["OR"], 257.95)

    # Ben commission
    # = 5159 / 2 * 5% + 4147GBP * 5% + 1056GBP * 5% + HU2 * 3
    # = 519.858
    assert math.isclose(commissions["Ben"], 519.858)


def test_sales_commissions2():
    sales_list = parse_sales_list(sales_testdata.sales, 1)

    currencies = sales_testdata.test_currency_table

    commissions = calculate_commissions2(sales_list, currencies, bonus_rates)

    assert isinstance(commissions, list)
    assert len(commissions) == 7
    # sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <E> <Ben> <E> <Corey>"
    # sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
    # sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <SG> <Alex>"
    # sale4 = "<HU2JAIL> <49> <USD> <example@email.com> <N> <Ben>"
    # sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"
    # sale6 = "<WR full> <4147> <GBP> <N>  <foobar@live.co.uk> <MJR>🚨"

    # Seller,Product,Price,Currency,Customer,Bonus,Splits,Conversion,Commission

    # First results - Ben and Corey split a sale
    n = 0
    assert commissions[n]["Seller"] == "Ben"
    assert commissions[n]["Product"] == "WR"
    assert math.isclose(commissions[n]["Price"], 4056.0)
    assert commissions[n]["Currency"] == "GBP"
    assert commissions[n]["Customer"] == "joker@gmail.com"
    assert commissions[n]["Bonus"] == "E"
    assert commissions[n]["Splits"] == 2
    assert commissions[n]["Conversion"] == 1.22
    assert math.isclose(commissions[n]["Commission"], 173.1912)

    n = 1
    assert commissions[n]["Seller"] == "Corey"
    assert commissions[n]["Product"] == "WR"
    assert math.isclose(commissions[n]["Price"], 4056.0)
    assert commissions[n]["Currency"] == "GBP"
    assert commissions[n]["Customer"] == "joker@gmail.com"
    assert commissions[n]["Bonus"] == "E"
    assert commissions[n]["Splits"] == 2
    assert commissions[n]["Conversion"] == 1.22
    assert math.isclose(commissions[n]["Commission"], 173.1912)

    # Second sale - HU2
    n = 2
    assert commissions[n]["Seller"] == "Alex"
    assert commissions[n]["Product"] == "HU2"
    assert math.isclose(commissions[n]["Price"], 49.0)
    assert commissions[n]["Currency"] == "USD"
    assert commissions[n]["Customer"] == "hustler@foobar.edu"
    assert commissions[n]["Bonus"] == "N"
    assert commissions[n]["Splits"] == 1
    assert commissions[n]["Conversion"] == 1.0
    assert math.isclose(commissions[n]["Commission"], 24.5)

    # Fourth sale - use HU2JAIL case
    # sale4 = "<HU2JAIL> <49> <USD> <example@email.com> <N> <Ben>"
    n = 4
    assert commissions[n]["Seller"] == "Ben"
    assert commissions[n]["Product"] == "HU2JAIL"
    assert math.isclose(commissions[n]["Price"], 49.0)
    assert commissions[n]["Currency"] == "USD"
    assert commissions[n]["Customer"] == "example@email.com"
    assert commissions[n]["Bonus"] == "N"
    assert commissions[n]["Splits"] == 1
    assert commissions[n]["Conversion"] == 1.0
    assert math.isclose(commissions[n]["Commission"], 24.5)

    # Fifth sale - check "HU" case
    # sale5 = "<HU> <39.80> <GBP> <example@email.uk> <N> <Alex>"
    n = 5
    assert commissions[n]["Seller"] == "Alex"
    assert commissions[n]["Product"] == "HU"
    assert math.isclose(commissions[n]["Price"], 39.80)
    assert commissions[n]["Currency"] == "GBP"
    assert commissions[n]["Customer"] == "example@email.uk"
    assert commissions[n]["Bonus"] == "N"
    assert commissions[n]["Splits"] == 1
    assert commissions[n]["Conversion"] == 1.22
    assert math.isclose(commissions[n]["Commission"], 24.278)
