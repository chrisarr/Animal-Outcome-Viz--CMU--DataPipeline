import csv
import httplib2
from apiclient.discovery import build
import urllib
import json

# This API key is provided by google as described in the tutorial
API_KEY = "AIzaSyCtw2c6LVCpUq3xYr4fnMm5fmVhOiyWMvI"
# This is the table id for the fusion table
TABLE_ID = "19UEOL4eYHM1FzSAReEy0j2vwh6DsDUHhprZ9kuby"

service = build('fusiontables', 'v1', developerKey=API_KEY)

# query = "SELECT * FROM " + TABLE_ID + " WHERE type = 'DOG'"
# response = service.query().sql(sql=query).execute()

# all_dogs = "SELECT * FROM " + TABLE_ID + " WHERE type = 'DOG'"
# all_dogs = service.query().sql(sql=str(all_dogs)).execute()

# outcomes = []
# for row in all_dogs['rows'][0:25]:
# 	if row[13] not in outcomes:
# 		outcomes.append(row[13])
# 	else: continue
# print outcomes

query = "SELECT * FROM " + TABLE_ID
response = service.query().sql(sql=query).execute()

rows = response['rows']

types = [u'DOG', u'CAT', u'OTHER', u'LIVESTOCK', u'BIRD', u'GUINEA PIG', u'RABBIT']


########################################################################
# Byte 3 Exploration Code 
########################################################################

# all results
clean_results = [{'type':row[1].encode('utf-8'), 'date':row[2][0:7].encode('utf-8'), 'outcome':row[13].encode('utf-8')} for row in rows]

import operator

# Remove animals returned to owners, as these were planned visits
# and our data is looking at animals without homes at time of admittence
clean_results = [animal for animal in clean_results if animal['outcome'] != 'Returned to Owner']

# Remove livestock, as we are interested in domesticated, adoptable animals
clean_results = [animal for animal in clean_results if animal['type'] != 'LIVESTOCK']

# This generates a dateset of all animals of all outcome 
# types tracked by month, for each year in the data.

# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['date'] == date])
# print dates

# code commented out above
date_totals = {'2011-08': 1147, '2011-09': 829, '2011-02': 683, '2011-03': 863, '2011-01': 739, '2011-06': 1161, '2011-07': 1154, '2011-04': 1039, '2011-05': 1111, '2012-10': 91, '2011-11': 707, '2011-10': 689, '2011-12': 680, '2012-09': 753, '2012-08': 914, '2012-03': 747, '2012-02': 586, '2012-01': 596, '2012-07': 960, '2012-06': 1002, '2012-05': 927, '2012-04': 902}

# # Dogs totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'DOG' and a['date'] == date])
# print dates

# code above
dog_date_totals = {'2011-08': 456, '2011-09': 291, '2011-02': 378, '2011-03': 451, '2011-01': 389, '2011-06': 466, '2011-07': 462, '2011-04': 458, '2011-05': 471, '2012-10': 26, '2011-11': 368, '2011-10': 249, '2011-12': 349, '2012-09': 317, '2012-08': 452, '2012-03': 389, '2012-02': 311, '2012-01': 304, '2012-07': 419, '2012-06': 363, '2012-05': 342, '2012-04': 350}

# # # Dogs adoption totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'DOG' and a['outcome'] == 'Adopted' and a['date'] == date])
# print dates

dog_date_adopts = {'2011-08': 116, '2011-09': 72, '2011-02': 99, '2011-03': 85, '2011-01': 118, '2011-06': 163, '2011-07': 129, '2011-04': 89, '2011-05': 155, '2012-10': 4, '2011-11': 112, '2011-10': 74, '2011-12': 79, '2012-09': 61, '2012-08': 73, '2012-03': 116, '2012-02': 104, '2012-01': 86, '2012-07': 95, '2012-06': 81, '2012-05': 108, '2012-04': 101}

# # Cat totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'CAT' and a['date'] == date])
# print dates

# code above
cat_date_totals = {'2011-08': 673, '2011-09': 506, '2011-02': 262, '2011-03': 368, '2011-01': 314, '2011-06': 679, '2011-07': 674, '2011-04': 499, '2011-05': 611, '2012-10': 62, '2011-11': 316, '2011-10': 425, '2011-12': 290, '2012-09': 396, '2012-08': 430, '2012-03': 294, '2012-02': 256, '2012-01': 252, '2012-07': 486, '2012-06': 586, '2012-05': 540, '2012-04': 443}

# # # Cat adoption totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'CAT' and a['outcome'] == 'Adopted' and a['date'] == date])
# print dates

cat_date_adopts = {'2011-08': 81, '2011-09': 47, '2011-02': 55, '2011-03': 31, '2011-01': 54, '2011-06': 131, '2011-07': 100, '2011-04': 84, '2011-05': 103, '2012-10': 3, '2011-11': 53, '2011-10': 67, '2011-12': 78, '2012-09': 28, '2012-08': 55, '2012-03': 47, '2012-02': 71, '2012-01': 69, '2012-07': 77, '2012-06': 99, '2012-05': 71, '2012-04': 72}

# # Bird totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'BIRD' and a['date'] == date])
# print dates

# code above
bird_date_totals = {'2011-08': 6, '2011-09': 4, '2011-02': 3, '2011-03': 5, '2011-01': 9, '2011-06': 4, '2011-07': 3, '2011-04': 21, '2011-05': 3, '2012-10': 0, '2011-11': 0, '2011-10': 4, '2011-12': 5, '2012-09': 9, '2012-08': 13, '2012-03': 10, '2012-02': 0, '2012-01': 5, '2012-07': 10, '2012-06': 17, '2012-05': 20, '2012-04': 56}

# # # Bird adoption totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'BIRD' and a['outcome'] == 'Adopted' and a['date'] == date])
# print dates

bird_date_adopts = {'2011-08': 0, '2011-09': 0, '2011-02': 0, '2011-03': 0, '2011-01': 0, '2011-06': 0, '2011-07': 0, '2011-04': 0, '2011-05': 0, '2012-10': 0, '2011-11': 0, '2011-10': 0, '2011-12': 0, '2012-09': 0, '2012-08': 0, '2012-03': 0, '2012-02': 0, '2012-01': 2, '2012-07': 1, '2012-06': 0, '2012-05': 0, '2012-04': 0}

# # Rabbit totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'RABBIT' and a['date'] == date])
# print dates

# code above
rabbit_date_totals = {'2011-08': 0, '2011-09': 0, '2011-02': 0, '2011-03': 0, '2011-01': 0, '2011-06': 0, '2011-07': 0, '2011-04': 0, '2011-05': 0, '2012-10': 0, '2011-11': 6, '2011-10': 2, '2011-12': 10, '2012-09': 6, '2012-08': 2, '2012-03': 9, '2012-02': 2, '2012-01': 3, '2012-07': 2, '2012-06': 2, '2012-05': 5, '2012-04': 8}

# # # Rabbit adoption totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'RABBIT' and a['outcome'] == 'Adopted' and a['date'] == date])
# print dates

rabbit_date_adopts = {'2011-08': 0, '2011-09': 0, '2011-02': 0, '2011-03': 0, '2011-01': 0, '2011-06': 0, '2011-07': 0, '2011-04': 0, '2011-05': 0, '2012-10': 0, '2011-11': 2, '2011-10': 0, '2011-12': 0, '2012-09': 2, '2012-08': 1, '2012-03': 2, '2012-02': 1, '2012-01': 0, '2012-07': 2, '2012-06': 1, '2012-05': 0, '2012-04': 1}

# # GUINEA totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'GUINEA PIG' and a['date'] == date])
# print dates

# code above
guinea_date_totals = {'2011-08': 0, '2011-09': 7, '2011-02': 0, '2011-03': 0, '2011-01': 0, '2011-06': 0, '2011-07': 0, '2011-04': 0, '2011-05': 0, '2012-10': 0, '2011-11': 3, '2011-10': 0, '2011-12': 2, '2012-09': 1, '2012-08': 0, '2012-03': 0, '2012-02': 0, '2012-01': 0, '2012-07': 1, '2012-06': 0, '2012-05': 3, '2012-04': 0}

# # # GUINEA adoption totals
# dates = {}
# for a in clean_results:
# 	if a['date'] not in dates and a['date'] != 0:
# 		this_date = a['date']
# 		dates[this_date] = 0
# for date, v in dates.iteritems():
# 	dates[date] = len([a for a in clean_results if a['type'] == 'GUINEA PIG' and a['outcome'] == 'Adopted' and a['date'] == date])
# print dates

guinea_date_adopts = {'2011-08': 0, '2011-09': 2, '2011-02': 0, '2011-03': 0, '2011-01': 0, '2011-06': 0, '2011-07': 0, '2011-04': 0, '2011-05': 0, '2012-10': 0, '2011-11': 0, '2011-10': 0, '2011-12': 0, '2012-09': 0, '2012-08': 0, '2012-03': 0, '2012-02': 0, '2012-01': 0, '2012-07': 0, '2012-06': 0, '2012-05': 0, '2012-04': 0}

types_sorted = ['date', 'dogs_total', 'dogs_adopted', 'cats_total', 'cats_adopted','rabbits_total','rabbits_adopted','birds_total','birds_adopted','guinea_pigs_total','guinea_pigs_adopted']

dates_sorted = [['2011-01'], ['2011-02'], ['2011-03'], ['2011-04'], ['2011-05'], ['2011-06'], ['2011-07'], ['2011-08'], ['2011-09'], ['2011-10'], ['2011-11'], ['2011-12'], ['2012-01'], ['2012-02'], ['2012-03'], ['2012-04'], ['2012-05'], ['2012-06'], ['2012-07'], ['2012-08'], ['2012-09'], ['2012-10']]

for date in dates_sorted:
	for entry, v in dog_date_totals.iteritems():
		if entry == date[0]:
			date.append(v)
	for entry, v in dog_date_adopts.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in cat_date_totals.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in cat_date_adopts.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in rabbit_date_totals.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in rabbit_date_adopts.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in bird_date_totals.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in bird_date_adopts.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in guinea_date_totals.iteritems():
		if entry == date[0]:
			date.append(v)

	for entry, v in guinea_date_adopts.iteritems():
		if entry == date[0]:
			date.append(v)

print dates_sorted

# import numpy
# numpy.savetxt("foo.csv", a, delimiter=",")


# data = sorted(data, key=lambda x: dates_sorted.index(x['date']))
# data = numpy.asarray(data)

# print data


########################################################################
# Byte 2 Exploration Code 
########################################################################

# # Euthanized dogs by age
# ages_over_7_all = "SELECT * FROM " + TABLE_ID + " WHERE type = 'DOG' AND age = 'Older than 7 years'"
# younger_6_mo_all = "SELECT * FROM " + TABLE_ID + " WHERE type = 'DOG' AND age = 'Infant - Younger than 6 months'"
# older_1_year_all = "SELECT * FROM " + TABLE_ID + " WHERE type = 'DOG' AND age = 'Older than 1 year'"
# younger_1_yr_all = "SELECT * FROM " + TABLE_ID + " WHERE type = 'DOG' AND age = 'Youth - Younger than 1 year'"
# unknown_age = "SELECT * FROM " + TABLE_ID + " WHERE type = 'DOG' AND age = ''"

# all_results = {"Over 7 years old": ages_over_7_all, "Infant - Younger than 6 months": younger_6_mo_all, "Older than 1 year": older_1_year_all, "Youth - Younger than 1 year": younger_1_yr_all, "Age unknown": unknown_age}




# # >>>>>>>>> Plotting <<<<<<<<<<<

# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt

# cols = [entry for entry in all_results]
# rows = [int(len(service.query().sql(sql=v).execute()['rows'])) for k, v in all_results.iteritems()] 

# x_pos = np.arange(len(cols))

# p1 = plt.bar(x_pos, rows, color="blue", alpha=1, label="total")

# cols = [entry for entry in all_results]
# #### Euthanized Dogs
# rows = [int(len(service.query().sql(sql=str(v + "AND outcome = 'Euthanized'")).execute()['rows'])) for k, v in all_results.iteritems()] 
# p2 = plt.bar(x_pos, rows, color="red", alpha=1, label="euthanized")

# # #### Returned to Owner Dogs
# # rows = [int(len(service.query().sql(sql=str(v + "AND outcome = 'Returned to Owner'")).execute()['rows'])) for k, v in all_results.iteritems()] 
# # p2 = plt.bar(x_pos, rows, color="red", alpha=1, label="returned")

# # #### Adopted Dogs
# # rows = [int(len(service.query().sql(sql=str(v + "AND outcome = 'Adopted'")).execute()['rows'])) for k, v in all_results.iteritems()] 
# # p2 = plt.bar(x_pos, rows, color="red", alpha=1, label="adopted")

# # #### Transferred to Rescure Group Dogs
# # rows = [int(len(service.query().sql(sql=str(v + "AND outcome = 'Transferred to Rescue Group'")).execute()['rows'])) for k, v in all_results.iteritems()] 
# # p2 = plt.bar(x_pos, rows, color="red", alpha=1, label="transferred")

# x_pos = np.arange(len(rows))

# plt.xticks(x_pos, cols, rotation=45)
# plt.yticks()
# plt.legend(loc='upper right')

# plt.subplots_adjust(bottom=0.4)

# plt.show()





