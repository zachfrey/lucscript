
# Sales type determines commission rate:
#
# N  = No bonus = 5%
# SG = Self generated = 10%
# E  = Eli = 7%

sale1 = "<WR> <4056> <GBP> <joker@gmail.com> <E> <Ben> <Corey>"
sale2 = "<HU2> <49> <USD> <hustler@foobar.edu> <N> <Alex>"
sale3 = "<WR> <4997> <USD> <hustler@foobar.edu> <SG> <Alex>"
sale4 = "<HU2> <49> <USD> <example@email.com> <N> <Ben>"
sale5 = "<HU2> <39.80> <GBP> <example@email.uk> <N> <Alex>"

sales = sale1 + "," + sale2 + "," + sale3 + "," + sale4 + "," + sale5

currency_table_keys = ["USD", "GBP"]
currency_table_values = [1.0, 1.22]
test_currency_table = dict(zip(currency_table_keys, currency_table_values))

commissions_keys = ["Alex", "Ben", "Corey"]
commissions_values = [0.05, 0.04, 0.06]
test_commissions = dict(zip(commissions_keys, commissions_values))