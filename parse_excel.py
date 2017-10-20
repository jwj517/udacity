#!/usr/bin/env python3
#_*_coding:utf-8 _*_

import xlrd

datafile = "/Users/jingweijie/Documents/数据分析进阶之纳米学位/lesson2/Book21017.xlsx"

def parse_file(datafile):
	workbook = xlrd.open_workbook(datafile)
	sheet = workbook.sheet_by_index(0)
	print(workbook.sheet_names())
	data = [[sheet.cell_value(r,col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
	print("\nList Comprehension")
	print("data[3][2]:,")
	print(data[3][2])

	print("\nCells in a nested loop:")
	for row in range(sheet.nrows):
		for col in range(sheet.ncols):
			if row == 50:
				print(sheet.cell_value(row,col))

	print("\nROWS, COLUMNS, and CELLS:")
	print("Number of rows in the sheet:")
	print(sheet.nrows)
	print(sheet.ncols)
	print("Type of data in cell(row 3, col 2):")
	print(sheet.cell_type(3,2))
	print("Value in cell(row 3, col 2):")
	print(sheet.cell_value(3,2))
	print("Get a slice of valiues in column 3, from rows 1-3:")
	print(sheet.col_values(3,start_rowx=1,end_rowx=4))
	print(sheet.row_values(3,start_colx=1,end_colx=4))
	print("\nDATES:")
	print("Type of data in cell(row 1, col 0):")
	print(sheet.cell_type(1,0))
	exceltime = sheet.cell_value(1,0)
	print("Time in excel format:%s" % exceltime)
	print(xlrd.xldate_as_tuple(exceltime,0))

	return data

data = parse_file(datafile)