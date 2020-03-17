import csv
from prettytable import PrettyTable
import sys
import matplotlib.pyplot as plt
import numpy as np

case_totals_file = "total-cases-covid-19-who.csv"
countries_dict = {}
output_headers = ["Days in", "Cases", "Percentage Increase"]
formatter = PrettyTable(output_headers)

if sys.argv[1]:
	lookup_coutry = sys.argv[1]
else:
	lookup_coutry = "United States"

def make_plot(cases_by_day):
	plt.figure()
	days = [ int(data["days_in"]) for data in cases_by_day]
	percent_increases = [ data["percent_increase"] for data in cases_by_day]
	plt.plot(days, percent_increases)  

	plt.xlabel("Days since first infection")
	plt.ylabel("Percentage increase over previous day")
	plt.title("Percentage of spread in " + lookup_coutry)

	plt.savefig('growth_rate.png')

def get_previous_day_increase(current, previous):
	diff = current - previous
	return round((diff / current) * 100, 3)

def parse_country(countries_dict, row):
	country = row[0]
	days_in = row[2]
	cases = row[3]
	if int(cases) < 20: return True 
	if country in countries_dict:
		previous_day = countries_dict[country][-1]
		countries_dict[country].append({ 
			"days_in" 		   : days_in, 
			"cases"            : cases,
			"percent_increase" : get_previous_day_increase(int(cases), int(previous_day["cases"]))
		})
	else:
		countries_dict[country] = [
		 { "days_in" : days_in, "cases" : cases, "percent_increase" : 0.0 }
		]

with open(case_totals_file, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(csvreader)
	for row in csvreader:	
		parse_country(countries_dict, row)	
	us_cases_by_day = countries_dict[lookup_coutry]

	for daily_cases in us_cases_by_day:
		formatter.add_row([
			daily_cases["days_in"], 
			daily_cases["cases"], 
			daily_cases["percent_increase"]
		])
	make_plot(us_cases_by_day)
	print(formatter)

