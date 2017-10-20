#!/usr/bin/env python3
#_*_coding:utf-8_*_

import os


DATADIR = "/Users/jingweijie/Documents/数据分析进阶之纳米学位/lesson2"
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
	data = []
	with open(datafile,"r") as f:
		header = f.readline().split(",")
		counter = 0
		for line in f:
			if counter == 10:
				break
			print(line)
			fields = line.split(",")
			print(fields)
			entry = {}
			for i,value in enumerate(fields):
				entry[header[i].strip()] = value.strip()
			data.append(entry)
			counter = counter+1
	return data

def test():
	datafile = os.path.join(DATADIR,DATAFILE)
	d = parse_file(datafile)
	firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
	tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
	print(d[0])
	print(d[9])
	assert d[0] == firstline
	assert d[9] == tenthline

if __name__ == '__main__':
	test()