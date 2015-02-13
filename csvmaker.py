data = [['2011-01', 389, 118, 314, 54, 0, 0, 9, 0, 0, 0], ['2011-02', 378, 99, 262, 55, 0, 0, 3, 0, 0, 0], ['2011-03', 451, 85, 368, 31, 0, 0, 5, 0, 0, 0], ['2011-04', 458, 89, 499, 84, 0, 0, 21, 0, 0, 0], ['2011-05', 471, 155, 611, 103, 0, 0, 3, 0, 0, 0], ['2011-06', 466, 163, 679, 131, 0, 0, 4, 0, 0, 0], ['2011-07', 462, 129, 674, 100, 0, 0, 3, 0, 0, 0], ['2011-08', 456, 116, 673, 81, 0, 0, 6, 0, 0, 0], ['2011-09', 291, 72, 506, 47, 0, 0, 4, 0, 7, 2], ['2011-10', 249, 74, 425, 67, 2, 0, 4, 0, 0, 0], ['2011-11', 368, 112, 316, 53, 6, 2, 0, 0, 3, 0], ['2011-12', 349, 79, 290, 78, 10, 0, 5, 0, 2, 0], ['2012-01', 304, 86, 252, 69, 3, 0, 5, 2, 0, 0], ['2012-02', 311, 104, 256, 71, 2, 1, 0, 0, 0, 0], ['2012-03', 389, 116, 294, 47, 9, 2, 10, 0, 0, 0], ['2012-04', 350, 101, 443, 72, 8, 1, 56, 0, 0, 0], ['2012-05', 342, 108, 540, 71, 5, 0, 20, 0, 3, 0], ['2012-06', 363, 81, 586, 99, 2, 1, 17, 0, 0, 0], ['2012-07', 419, 95, 486, 77, 2, 2, 10, 1, 1, 0], ['2012-08', 452, 73, 430, 55, 2, 1, 13, 0, 0, 0], ['2012-09', 317, 61, 396, 28, 6, 2, 9, 0, 1, 0], ['2012-10', 26, 4, 62, 3, 0, 0, 0, 0, 0, 0]]

import os
import csv

f = open(os.path.join("data/data.csv"), 'a+')

headers = ['date', 'dogs_total', 'dogs_adopted', 'cats_total', 'cats_adopted','rabbits_total','rabbits_adopted','birds_total','birds_adopted','guinea_pigs_total','guinea_pigs_adopted']

csv_writer = csv.writer(f, delimiter=',', lineterminator='\r\n')

f.seek(0,0) # Jump to beginning, to see if we have headers

csv_writer.writerow([title for title in headers]) # Write headers into first row
for row in data:
	csv_writer.writerow(row) # Write headers into first row

f.close()
