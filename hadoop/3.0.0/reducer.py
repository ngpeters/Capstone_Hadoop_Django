#! /usr/bin/env python

import sys

last_profit_method = None
profit_method_count = 0

# Example input (notice how they're IN ORDER):
# FALSE 1
# FALSE 1

for line in sys.stdin:

    line = line.strip()
    profit_method, count = line.split("\t")

    count = int(count)
    # if this is the first iteration
    if not last_profit_method:
        last_profit_method = profit_method

    # if they're the same, log it
    if profit_method == last_profit_method:
        profit_method_count += count
    else:
        # 
        result = [last_profit_method, profit_method_count]
        print("\t".join(str(v) for v in result))
        last_profit_method = profit_method
        profit_method_count = 1

# this is to catch the final value that we output
print("\t".join(str(v) for v in [last_profit_method, profit_method_count]))