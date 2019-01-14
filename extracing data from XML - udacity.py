#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys

import xml.etree.ElementTree as ET

article_file = "exampleresearcharticle.xml"

def get_root(filename):
	tree = ET.parse(filename)
	return tree.getroot()


def get_authors(root):
	# create a list of dictionaries
	authors=[]
	# use the findall method to extract all elements under particular tag
	author_tag = root.findall('./fm/bibl/aug/au')
	for author in author_tag:
		#create an empty list of dictionaries with the keys defined
		data = {
				"snm": None,
				"fnm": None,
				"email": None,
				"insr": []
		}
		data['snm']=author.find('./snm').text
		data['fnm']=author.find('./fnm').text
		data['email']=author.find('./email').text
		#extracting the attribute name value pairs for insr tag into a list for each author
		insr = author.findall('./insr')
		for i in insr:
			data['insr'].append(i.attrib['iid'])
		authors.append(data)
	return authors	


def test():

	root = get_root(article_file)
	data = get_authors(root)
	print("data as follows \n")	
	print(data)

	print("Assertion test")
	solution = [{'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
                {'insr': ['I2'], 'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
                {'insr': ['I3', 'I4'], 'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
                {'insr': ['I3'], 'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
                {'insr': ['I8'], 'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
                {'insr': ['I3', 'I5'], 'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
                {'insr': ['I6'], 'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
                {'insr': ['I7'], 'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
	assert data[0] == solution[0]
	assert data[1]["fnm"] == solution[1]["fnm"]
	assert data[1]["insr"] == solution[1]["insr"]
	print("Assertion test successful")


if __name__=="__main__":
	test()