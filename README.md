# lucscript
Scripts for Luc

From Telegram:

> So basically, I manage a sales team \
> And every month I need to calculate their commissions \
> Sometimes multiple salesmen contribute to the same sale \
> &lt;example product&gt; &lt;997&gt; &lt;GBP&gt; &lt;example@email&gt; &lt;N&gt; &lt;Ben&gt; &lt;Corey&gt; \
> This is an example string I’ll receive as input \
> I’ll be working with a list of these strings in a csv \
> First thing I’d need to do, is create a csv for each salesman \
> So I have every sale Corey has made for example \
> Next I’ll need to run some equations to calculate the commission per sale \
> For example, Corey has a base 5% commission \
> But since Corey AND Ben made the sale
> Corey’s commission is split in 2 \

Special case: Commission for HU2 is always 50%

Testing

1. Install pytest

2. Add script directory to PYTHONPATH

3. Run pytest (no arguments)
