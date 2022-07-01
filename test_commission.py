from commission import *
from readsales import parse_sales_list
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
