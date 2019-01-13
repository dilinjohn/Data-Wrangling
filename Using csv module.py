import os
import csv

DATAFILE = "beatles-diskography.csv"
DATADIR = "C:\\Users\\dkaithav\\Downloads\\"

def parse_csv(datafile):
	data=[]
	with open(datafile, "r") as f:
		# using the csv dictreader assumes that the first line is the header
		r = csv.DictReader(f)
		for line in r: # each line is a dictionary
			data.append(line)
		return data


if __name__ == "__main__":
	datafile = os.path.join(DATADIR, DATAFILE)
	d = parse_csv(datafile)
	print(d[14])

