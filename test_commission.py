from commission import *
from readsales import parse_sales_list

import sales_testdata

#sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <N> <Ben> <Corey>"
#sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
#sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <N> <Alex>"
#sale4 = "<HU2> <49> <USD> <example@email.com> <N> <Ben>"
#sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"

#sales = sale1 + "," + sale2 + "," + sale3 + "," + sale4 + "," + sale5

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

    # Ben's sales: 2028 GBP + 49 USD = 2,523.16 USD
    assert totals["Ben"] == 2523.16

    # Corey's sales: 2028 GBP * 1.22 conversion = 2,474.16 USD
    assert totals["Corey"] == 2474.16