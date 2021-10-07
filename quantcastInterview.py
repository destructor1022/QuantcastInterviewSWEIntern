import sys
from optparse import OptionParser
import csv
from quantcastFunctions import *

csv_name = sys.argv[1]

parser = OptionParser()
parser.add_option('-d',dest = 'date')
(options,args) = parser.parse_args()

date = options.date

contents = []
with open(csv_name, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        contents.append(row)

counts_list = {}

for row in contents:
	if correct_date(row[1], date):
		increment_count(counts_list, row[0])

cookie_list = find_max_cookie(counts_list)
for cookie in cookie_list:
    print(cookie)