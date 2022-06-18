sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <N> <Ben> <Corey>"
sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <N> <Alex>"
sale4 = "<HU2> <49> <USD> <example@email.com> <N> <Ben>"
sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"

sales = sale1 + "," + sale2 + "," + sale3 + "," + sale4 + "," + sale5

currency_table_keys = ["USD", "GBP"]
currency_table_values = [1.0, 1.22]
test_currency_table = dict(zip(currency_table_keys, currency_table_values))