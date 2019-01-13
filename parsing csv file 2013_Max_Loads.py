
# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import os
import xlrd
import csv
import numpy as np
from zipfile import ZipFile


DATAFILE="2013_ERCOT_Hourly_Load_Data.zip"
DATADIR="C:\\Users\\dkaithav\\Downloads\\Sublime Text Build 3126 x64\\"

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"

path= os.getcwd()+'\\'+DATAFILE
print(path)

# Open the zip file

def open_zip(path):
	with ZipFile(path, 'r') as zf:
		#print all contents of the file
		zf.printdir()
		# extract all file contents
		zf.extractall()
		print("Done")
			
		
def parse_file(datafile):
	# open the workbook
	workbook=xlrd.open_workbook(datafile)
	sheet= workbook.sheet_by_index(0)
	# read the contents of the sheet
	print("number of rows is {} and columns is {}".format(sheet.nrows, sheet.ncols))
	data=[['Station', 'Year','Month', 'Day', 'Hour', 'Max Load']]
	# reading the data into a python list
	# data = [[sheet.cell_value(row, col)
	#  			for col in range(sheet.ncols)]
	#  				for row in range(1)]
	# print(data)

 	# check the max values in each column
	for i in range(1, sheet.ncols-1):
		# retrive the index of the highest value
		col_vals=sheet.col_values(i, start_rowx=1, end_rowx=None)
		max_col_val = max(col_vals)
		max_pos = col_vals.index(max_col_val) + 1
		#print(max_pos)
		max_time = sheet.cell_value(max_pos,0)
		(year, month, day, hour,_,_ ) = xlrd.xldate_as_tuple(max_time,0)
		station = sheet.cell_value(0, i)
		data.append([station, year, month, day, hour, max_col_val])
	#print(data)
	return(data)


def save_file(data, filename):
	with open(filename, 'w') as f:
		writer=csv.writer(f, delimiter="|") # create the file object
		for row in data:
			writer.writerow(row)
			#print(row)

def read_file(filename):
	print("\n\n")
	with open(filename, 'r') as f:
		print(f.read()) # reads the entire contents of the file in one go

def test():
	open_zip(path)
	data= parse_file(datafile)
	print(data)
	save_file(data, outfile)
	read_file(outfile)



	# with open(outfile) as f:
	# 	csvfile = csv.writer(f, delimiter="|")
	#  	for line in csvfile:
	# 		print(line)


if __name__ == "__main__":
	test()

#open_zip(path)
#parse_file(datafile)



