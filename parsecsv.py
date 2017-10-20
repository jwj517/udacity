#!/usr/bin/env python3
#_*_coding:utf-8 _*_

import os
import csv

DATADIR = "/Users/jingweijie/Documents/数据分析进阶之纳米学位/lesson2"
DATAFILE = "beatles-diskography.csv"

def parse_csv(datafile):
	data = []
	n = 0
	with open(datafile,encoding = 'utf-8') as sd:
		r = csv.DictReader(sd)
		for line in r:
			if n == 10:
				break
			data.append(line)
			n = n + 1
	return data

if __name__ == '__main__':
	datafile  = os.path.join(DATADIR,DATAFILE)
	d = parse_csv(datafile)
	firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
	tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
	#print(d[0])
	#print(d[9])
	assert d[0] == firstline
	assert d[9] == tenthline
	#print(d)