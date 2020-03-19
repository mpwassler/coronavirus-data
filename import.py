from datetime import date
from dateutil.rrule import rrule, DAILY
import requests
import os

start_date = date(2020, 1, 22)
today      = date.today()

# date = "1/22/2020"
def url_for_date(date):
	return "http://ncov.bii.virginia.edu/dashboard/data/nssac-ncov-sd-{date}.csv".format(date=date)

def get_file(date):	
	url = url_for_date(date)
	response = requests.get(url = url)
	if response:
		return response.text
	else:
		print(response, 'Faild to get file. ', url)
		return ""

def set_up_data_folder():
	dir_name = 'data'
	if not os.path.exists(dir_name):	    
		os.makedirs(dir_name)

def write_file(data, date):
	filename = "nssac-ncov-sd-{date}.csv".format(date=date)
	f = open("data/" + filename, "w")
	f.write(data)
	f.close()  

def import_data():
	for dt in rrule( DAILY, dtstart=start_date, until=today ):    	
		date = dt.strftime("%m-%d-%Y")
		data = get_file(date)
		write_file(data, date)

set_up_data_folder()
import_data()

