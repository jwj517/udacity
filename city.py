#!/usr/bin/env python3
#*_*coding:utf-8_*_

import xlrd
import os
import csv
from zipfile import ZipFile


datafile = "/Users/jingweijie/Documents/数据分析进阶之纳米学位/lesson2/Book21017.xlsx"
outfile = "/Users/jingweijie/Documents/数据分析进阶之纳米学位/lesson2/city.csv"

def open_zip(datafile):
	with ZipFile('{0}.zip'.format(datafile),'r') as myzip:
		myzip.extractall()

def parse_file(datafile):
	workbook = xlrd.open_workbook(datafile)
	sheet = workbook.sheet_by_index(0)
	data = []
	for row in range(sheet.nrows):
		row_list = []
		for col in range(sheet.ncols):
			row_list.append(sheet.cell_value(row,col))
		data.append(row_list)
	print(data)
	return data

def save_file(data,filename):
	with open(filename,'w') as f:
		writer = csv.writer(f,delimiter='|')
		for row in data:
			writer.writerow(row)

def test():
	data = parse_file(datafile)
	print(data)
	save_file(data, outfile)
	number_of_rows = 0
	stations = []
	ans = {'FAR_WEST': {'Max Load': '2281.2722140000024','Year': '2013','Month': '6','Day': '26','Hour': '17'}}
	correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH','NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
	fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']
	with open(outfile) as of:
		csvfile = csv.DictReader(of,delimiter="|")
		for line in csvfile:
			station = line['Station']
			if station == 'FAR_WEST':
				for field in fields:
					if field == 'Max Load':
						max_answer = round(float(ans[station][field]), 1)
						max_line = round(float(line[field]), 1)
						print(max_answer)
						print(max_line)
						assert max_answer == max_line
					else:
						assert ans[station][field] == line[field]
			number_of_rows += 1
			stations.append(station)
		assert number_of_rows == 8
		assert set(stations) == set(correct_stations)
test()