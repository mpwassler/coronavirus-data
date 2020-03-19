import csv
from prettytable import PrettyTable
import sys
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import re

data_folder = "./data"

if len(sys.argv) > 1:
	country = sys.argv[1]
else:
	country = "USA"

if len(sys.argv) > 2:
	state = sys.argv[2]
	mode = "state"
else:
	state = ""
	mode = "region"

def read_directory():
	return ["data/" + f for f in listdir(data_folder) if isfile(join(data_folder, f))]

def date_from_name(filename):
	match = re.search(r"(\d+-\d+-\d+)", filename) 
	return match.group(1)

def load_data():
	row_data = []
	for file in read_directory():
		date = date_from_name(file)
		with open( file, newline='') as csvfile:			
			csvreader = csv.reader( csvfile, delimiter=',', quotechar='|')
			next(csvreader)
			for row in csvreader:
				data = { "local": row[0], 
						 "region": row[1], 
						 "cases": row[3], 
						 "deaths": row[4], 
						 "recovered": row[5],
						 "date_reported": date}
				row_data.append(data)
	return row_data

def data_sorted_by(sort, data):
	data_by_local = {}
	for row in data:
		if row[sort] in data_by_local:
			data_by_local[row[sort]].append(row)
		else:
			data_by_local[row[sort]] = [row]
	return data_by_local

def get_total_for(value, items):
	return sum([ int(entry[value]) for entry in items ])

def get_previous_day_increase(current, previous):
	diff = current - previous
	if current == 0 or diff < 0:
		return 0
	return round((diff / current) * 100, 3)

def calulate_results_for_day(data, date, previous_day_data):
	daily_results = data[date]	
	cases = get_total_for("cases", daily_results)
	deaths = get_total_for("deaths", daily_results)
	recovered = get_total_for("recovered", daily_results)
	if previous_day_data:
		previous_day_cases = get_previous_day_increase(cases, previous_day_data["cases"])
		percent_new_deaths = get_previous_day_increase(deaths, previous_day_data["deaths"])
		percent_new_recovered = get_previous_day_increase(recovered, previous_day_data["recovered"])
	else:
		previous_day_cases = 0
		percent_new_deaths = 0
		percent_new_recovered = 0
	return {
			"date"                  : date,
			"cases"                 : cases,
			"deaths"                : deaths,
			"recovered"             : recovered,
			"percent_new_cases"     : previous_day_cases,
			"percent_new_deaths"    : percent_new_deaths,
			"percent_new_recovered" : percent_new_recovered,
			}

def totals_for_region(region_data):
	totals = []
	data_by_date = data_sorted_by("date_reported", region_data)
	dates = list(data_by_date.keys())
	dates.sort()
	for date in dates:
		if len(totals) > 0:
			previous_day_data = totals[-1]
		else:
			previous_day_data = None
		data = calulate_results_for_day(data_by_date, date, previous_day_data)	
		totals.append(data)
	return totals

def case_number_at_least(amount, data):
	return [row for row in data if row["cases"] >= amount]

def print_results_table(data):
	data = case_number_at_least(20, data)
	output_headers = ["Date", "Cases", "Cases % ^", "Deaths", "Deaths % ^", "Recovered", "Recovered % ^" ]
	formatter = PrettyTable(output_headers)
	for daily_cases in data:
		formatter.add_row([ daily_cases["date"], 
			                daily_cases["cases"], 
			                daily_cases["percent_new_cases"],
			                daily_cases["deaths"],
			                daily_cases["percent_new_deaths"],
			                daily_cases["recovered"],
			                daily_cases["percent_new_recovered"] ])
	print(formatter)


def draw_growth_plot(data):
	title = "Percentage of spread in " + country + " " +  state
	data = case_number_at_least(20, data)
	recovered =             [ row["recovered"]             for row in data ]
	percent_new_cases =     [ row["percent_new_cases"]     for row in data ]
	percent_new_deaths =    [ row["percent_new_deaths"]    for row in data ]
	percent_new_recovered = [ row["percent_new_recovered"] for row in data ]
	plt.figure()
	plt.plot( range(len(data)), percent_new_cases, 'b-',     label='Cases', linewidth=2 )
	plt.plot( range(len(data)), percent_new_deaths, 'r--',   label='Deaths' )	
	plt.plot( range(len(data)), percent_new_recovered, 'g:', label='Recoverd' )
	plt.legend()
	plt.xlabel("Days (of at least 20 cases)")
	plt.ylabel("Percentage increase over previous day")
	plt.title(title)
	plt.savefig('charts/growth_rate.png')

def draw_totals_plot(data):
	title = "Totals in " + country + " " +  state
	data = case_number_at_least(20, data)
	cases =                 [ row["cases"]                 for row in data ]
	deaths =                [ row["deaths"]                for row in data ]
	recovered =             [ row["recovered"]             for row in data ]
	plt.figure()
	plt.plot( range(len(data)), cases, 'b-',     label='Cases', linewidth=2 )
	plt.plot( range(len(data)), deaths, 'r--',   label='Deaths' )	
	plt.plot( range(len(data)), recovered, 'g:', label='Recoverd' )
	plt.legend()
	plt.xlabel("Days (of at least 20 cases)")
	plt.ylabel("Totals")

	plt.title(title)
	plt.savefig('charts/totals.png')

	

# load_date()
data = load_data()
if mode == "state":
	data_by_local = data_sorted_by("local", data)
	region_totals = totals_for_region(data_by_local[state])
else:
	data_by_local = data_sorted_by("region", data)
	region_totals = totals_for_region(data_by_local[country])

print_results_table(region_totals)
draw_growth_plot(region_totals)
draw_totals_plot(region_totals)