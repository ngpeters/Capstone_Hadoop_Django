#! /usr/bin/env python

import sys


# -- Compare Buyback Dividen data
# 


for line in sys.stdin:
	if ',' in line:
		line = line.strip()
		unpacked = line.split(",")
		index, buybackdate, buybackclose, dividendate, dividenclose = line.split(",")
		if (buybackclose > dividenclose):
			results = ["buyback", "1"]
		else:
			results = ["dividen", "1"]
		print("\t".join(results))
	else:
		print('fail')
