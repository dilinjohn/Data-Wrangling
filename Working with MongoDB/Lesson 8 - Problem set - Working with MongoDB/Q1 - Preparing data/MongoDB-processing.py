import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}

#print(FIELDS.values())
# FIELDS[key] retrieves the value associated with each key

def process_file(filename, fields):
   process_fields = fields.keys()
   data =[]
   
   with open('arachnid.csv', "r") as f:
      reader = csv.DictReader(f)
      for i in range(3):
         next(reader)
      for line in reader:
         line['rdf-schema#label'] = re.sub('\(.+\)', '', line['rdf-schema#label'].strip())

         if line['rdf-schema#label'] == 'NULL':
            line['rdf-schema#label'] = None

         if line['name'] == 'NULL' or re.search('\W+', line['name']):
            line['name'] = line['rdf-schema#label']


         if line['synonym'] == "NULL":
            line['synonym'] = None

         else:
            line['synonym']= parse_array(line['synonym'])
            for i in line['synonym']:
               i.replace("*", '')
         if line['family_label'] == 'NULL':
            line['family_label'] = None
         else:
            line['family_label'] = parse_array(line['family_label'])
            #print(line['family_label'])
         
         item ={}
         item['classification']={}

         for key in fields:
            if line[key] == 'NULL':
               line[key] = None

            if re.search(r'_label', key):
               item['classification'][fields[key]] = line[key]
            else:
               item[fields[key]] = line[key]
         data.append(item)
   return(data)     


def parse_array(v):
   if (v[0] == "{" and v[-1] == "}"):
      v = v.lstrip("{")
      v = v.rstrip("{")
      v_array = v.split("|")
      v_array = [v.strip() for v in v_array]
      return v_array
   return [v]



def test():
   data = process_file(DATAFILE, FIELDS)
   print("your first data")
   pprint.pprint(data[14])
   assert len(data) == 76
   #assert data[0] == first_entry
   assert data[17]["name"] == "Ogdenia"
   assert data[48]["label"] == "Hydrachnidiae"
   assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

if __name__ == "__main__":
   test()


