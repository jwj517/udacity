#!/usr/bin/env python3
#*_*coding:utf-8*_*

import xlrd
from zipfile import ZipFile

datafile = "/Users/jingweijie/Documents/数据分析进阶之纳米学位/lesson2/2013_ERCOT_Hourly_Load_Data.xls"

#def open_zip(datafile):
#	with ZipFile('{0}.zip'.format(datafile),'r') as myzip:
#		myzip.extractall()

def parse_file(datefile):
	workbook = xlrd.open_workbook(datafile)
	sheet = workbook.sheet_by_index(0)
	data = [[sheet.cell_value(r,col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
	cv = sheet.col_values(1,start_rowx=1, end_rowx=None)
	maxval = max(cv)
	print(maxval)
	minval = min(cv)
	maxpos = cv.index(maxval) + 1
	print(maxpos)
	minpos = cv.index(minval) + 1
	maxtime = sheet.cell_value(maxpos,0)
	mintime = sheet.cell_value(minpos,0)
	realtime = xlrd.xldate_as_tuple(maxtime,0)
	realmintime = xlrd.xldate_as_tuple(mintime,0)
	mintime = sheet.cell_value(minpos,0)
	data = {'maxtime':realtime,'maxvalue':maxval,'mintime':realmintime,'minvalue':minval,'avgcoast':sum(cv)/len(cv)}
	return data

def test():
#	open_zip(datafile)
	data = parse_file(datafile)
	print(data['maxtime'])
	assert data['maxtime']==(2013,8,13,17,0,0)
	print(data['maxvalue'])
	assert round(data['maxvalue'], 10) == round(18770.166858114047, 10)
test()

