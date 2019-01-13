# for excel files
import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

# define a function

def parse_file(datafile):
	workbook = xlrd.open_workbook(datafile)
	sheet = workbook.sheet_by_index(0) # open the first sheet
	# reading the data into a python list
	data = [[sheet.cell_value(row, col)
				for col in range(sheet.ncols)]
					for row in range(sheet.nrows)]

	print('\nList Comprehension')
	print('data[3][2]')
	print(data[3][2])
	print(sheet.cell_type(3,2))
	print('Getting a slice of values in columns from rows 1 to 3')
	print(sheet.col_values(3, start_rowx=1, end_rowx=4))
	print('headers')
	print(data[0][:])
	print("\n")
	print("Time in excel format")
	exceltime=sheet.cell_value(1,0)
	print(exceltime)
	print('Convert time to a Python datetime tuple, from Excel float')
	print(xlrd.xldate_as_tuple(exceltime, 0))

	return data


data = parse_file(datafile)