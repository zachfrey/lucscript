# lucscript
Sales Commission Scripts for Luc

1. Update the currency conversion file `currency/currency.csv`

Since commissions are calculated in U.S. dollars, you need to use the current
conversion factor from the currency (BTC, ETH, GBP, etc.) to USD.

2. Create a directory for this month's sales records

It's easiest to give each month its own directory as we will be splitting
into multiple files, one per seller

<pre>
mkdir <i>newfolder</i>
</pre>

3. Calculate the commission for each seller

<pre>
cd <i>newfolder</i>
../sales.py <i>salesdata.csv</i> ../currency/currency.csv <i>results.csv</i>
</pre>

Totals for each seller will be shown on the screen.

Detailed sales results are in *results.csv*

4. (Optional) Split the sales into per-seller files

These are CSV files for spreadsheet import.

<pre>
cd <i>newfolder</i>
../splitsales <i>salesdata.csv</i>
</pre>