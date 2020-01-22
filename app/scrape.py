from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re


def get_latest_date(url):
	""" Extracts the date from url of the latest bhav file """
	latest_date = re.findall('\d+', url.split('/')[-1:][0])[0]
	return latest_date


def get_latest_url():
	""" Returns the url of the latest bhav file from the webpage. """
	pagehtml = urlopen("https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx").read().decode('utf-8')
	soupdata = BeautifulSoup(pagehtml, 'html.parser')
	data = list(soupdata.find_all('a', attrs = {'id': "ContentPlaceHolder1_btnhylZip"}))
	url = data[0].attrs['href']
	return url

def get_latest_data(url):
	""" Returns parsed csv data downloaded from url. """
	resp = urlopen(url)

	if resp.getcode() != 200:
		print("HTTP Error!")
		return None

	csvdata = ""
	with ZipFile(BytesIO(resp.read())) as zipfile:
		with zipfile.open(zipfile.namelist()[0]) as file:
			csvdata=file.read().decode('utf-8')
	
	# print(csvdata.split('\r\n')[0])
	# print(len(csvdata.split('\r\n')[1:]))
	
	raw_data = [x.split(",") for x in csvdata.split('\r\n')[1:-1]]

	# Code: row[0]
	# Name: row[1]
	# Open: row[4]
	# High: row[5]
	# Low:  row[6]
	# Close:row[7]
	
	data = []
	# Removing irrelevent columns
	for row in raw_data:
		temp = []
		[ temp.append(row[i].strip()) for i in [0,1,4,5,6,7]]
		# for i in [0, 1, 4, 5, 6, 7]:
		# 	temp.append(row[i].strip())
		data.append(temp)
	return data
