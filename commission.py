import csv

# Sales type determines commission rate:
#
# N  = No bonus = 5%
# SG = Self generated = 10%
# E  = Eli = 7%

bonus_keys = ["N", "SG", "E"]
bonus_values = [0.05, 0.10, 0.07]
bonus_rates = dict(zip(bonus_keys, bonus_values))


# Read all lines from the sales file
def read_currency_conversion(fname):
    currency_table = dict()
    with open(fname) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            currency_table[row[0]] = row[1]
    return currency_table


# Calculate running commission total with bonus type
#     & currency conversion
# Returns - Dictionary indexed by name with commission total

def calculate_commissions(sales, currencies, sales_types):
    commissions = dict()
    for sale in sales:
        sellers = sale["seller"]
        num_sellers = len(sellers)
        line_number = sale["line_number"]
        # Convert currency to uppercase so that case won't matter
        # Strip leading and trailing whitespace, too
        currency = sale["currency"].strip().upper()
        price = sale["price"] / num_sellers
        if currency not in currencies:
            raise Exception(f"Line {line_number}: No currency conversion found for '{currency}'")
        price2 = price * float(currencies[currency])

        # Special case: commission for HU2 is always 50%

        for seller in sellers:
            # Error check for bonus
            sale_type = seller["bonus"]
            if sale_type not in sales_types:
                print(f"Line {line_number}: Invalid bonus type: '{sale_type}', no commission")
                commission = 0.0
            else:
                # Special case: commission for HU2 is always 50%
                if sale["product"][:2] == "HU":
                    commission = price2 * 0.5
                else:
                    commission = price2 * sales_types[sale_type]
            if seller["name"] not in commissions:
                commissions[seller["name"]] = commission
            else:
                commissions[seller["name"]] += commission
    return commissions


# Calculate running commission total with bonus type
#     & currency conversion
# Returns - List of dictionary objects representing rows in the output CSV
# Keys:Seller,Product,Price,Currency,Customer,Bonus,Splits,Conversion,Commission

def calculate_commissions2(sales, currencies, sales_types):
    sale_list = []

    for sale in sales:
        sellers = sale["seller"]
        num_sellers = len(sellers)
        line_number = sale["line_number"]
        if num_sellers == 0:
            print(f"Line {line_number}: no sellers found, cannot calculate commission")
            continue
        # Convert currency to uppercase so that case won't matter
        # Strip leading and trailing whitespace, too
        currency = sale["currency"].strip().upper()
        price = sale["price"] / num_sellers
        if currency not in currencies:
            raise Exception(f"Line {line_number}: No currency conversion found for '{currency}'")
        price2 = price * float(currencies[currency])

        for seller in sellers:
            newsale = dict()
            # Error check for bonus
            sale_type = seller["bonus"]
            if sale_type not in sales_types:
                print(f"Line {line_number}: Invalid bonus type: '{sale_type}', no commission")
                commission = 0.0
            else:
                # Special case: commission for HU2 is always 50%
                # Check beginning of string for HU to match
                if sale["product"][:2] == "HU":
                    commission = price2 * 0.5
                else:
                    commission = price2 * sales_types[sale_type]
            newsale["Seller"] = seller["name"]
            newsale["Product"] = sale["product"]
            newsale["Price"] = sale["price"]
            newsale["Currency"] = currency
            newsale["Customer"] = sale["email"]
            newsale["Bonus"] = sale_type
            newsale["Splits"] = num_sellers
            newsale["Conversion"] = float(currencies[currency])
            newsale["Commission"] = commission
            sale_list.append(newsale)

    return sale_list
