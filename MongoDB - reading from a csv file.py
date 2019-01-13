DATAFILE = "beatles-diskography.csv"
DATADIR = "C:\\Users\\dkaithav\\Downloads\\"

import os
print(os.getcwd())

# datafile = os.path.join(datadir, datafile)
# counter=0
# with open(datafile, "rb") as f:
# 	for line in f:
# 		print(line)
# 		counter+=1
# 		if counter > 5:
# 			print(counter)
# 			exit()


def parse_file(datafile):
	data = []
	with open(datafile, "r") as f:
		# read the headers
		header = f.readline().split(",")
		counter=0
		for line in f:
			if counter == 10:
				break
			fields = line.split(",")
			entry={}

			for i, values in enumerate(fields):
				entry[header[i].strip()] = values.strip()

			data.append(entry)
			counter += 1

	return data

def test():
	datafile = os.path.join(DATADIR, DATAFILE)
	d = parse_file(datafile)
	firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
	tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
	assert d[0] == firstline
	assert d[9] == tenthline
	print("No errors")

	print(d[:3])

test()