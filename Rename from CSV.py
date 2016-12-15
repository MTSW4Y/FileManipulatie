from shutil import copyfile
import csv

with open('namen.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
    	try:
    		copyfile(row[1], "SF/" + row[2])
    	except Exception as e:
    		print e, row[1]
