# lucscript
Sales Commission Scripts for Luc

1. Update the currency conversion file currency/currency.csv

Since commissions are calculated in U.S. dollars, you need to use the current
conversion factor from the currency (BTC, ETH, GBP, etc.) to USD.

2. Create a directory for this month's sales records

It's easiest to give each month its own directory as we will be splitting
into multiple files, one per seller

3. Calculate the commission for each seller

cd <newfolder>
../sales.py <salesdata.csv> ../currency/currency.csv <results.csv>

Totals for each seller will be shown on the screen.

Detailed sales results are in <results.csv>

4. (Optional) Split the sales into per-seller files

cd <newfolder>
../splitsales <salesdata.csv>