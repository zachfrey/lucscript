from commission import *
from readsales import parse_sales_list, read_sales
import math

import sales_testdata


def test_sales_commissions2():
    sales_list = parse_sales_list(sales_testdata.sales)

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
    sales = read_sales("Test2.csv")

    sales_list = []
    for line in sales:
        sales_list += parse_sales_list(line)

    currencies = sales_testdata.test_currency_table

    commissions = calculate_commissions(sales_list, currencies, bonus_rates)

    # TODO: Start asserting here

    # MJR commission:
    #   = Line with WR commission is bogus, so only HU2 commission
    #   = 28.5
    assert math.isclose(commissions["MJR"], 24.5)

    # Evo commission:
    #   = 3 HU2 commissions = 24.5 * 3
    assert math.isclose(commissions["Evo"], 73.5)

    # Check for bogus sellers
    assert "SG" not in commissions
