"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""

import csv
import os

DATADIR="C:\\Users\\dkaithav\\Downloads\\Sublime Text Build 3126 x64"
DATAFILE="745090.csv"

# with open(DATAFILE, 'r') as f:
# 	r = csv.reader(f) # read every line as a list of strings
# 	#print(next(r)) # prints the first line
# 	#print(next(r)) # prints the next line
# 	# print(next(r))
# 	# print(next(r))
# 	#next(r)
# 	# data= [row for row in r]
# 	# print(data)
# 	name=next(r)
# 	print("Name of the station is", name[1])
# 	header = next(r) # the next line which has the headers
# 	print('headers\n', header)
# 	print('\nData starts from here')
# 	data=[row for row in r] # actual data starts from here, but the iterator is now here
# 	print(data)

# putting this into a function

def parse_file(datafile):
	name=None
	header=None
	data=[]
	with open(datafile, 'r') as f:
		r = csv.reader(f)
		name=next(r)[1]
		print("Name of the station:", name)
		header=next(r)
		print('headers:\n', header)
		print('\nData starts from here')
		data=[row for row in r] # actual data starts from here, but the iterator is now here
		print("test data - first 3 lines")
		print(data[0:3])
	return(name, data)


def test():
	datafile=os.path.join(DATADIR, DATAFILE)
	name, data=parse_file(datafile)
	assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
	assert data[0][1] == "01:00"
	assert data[2][0] == "01/01/2005"
	assert data[2][5] == "2"
	print("No assertion errors recorded")

if __name__=="__main__":
 	test()




