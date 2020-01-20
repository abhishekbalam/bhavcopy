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
	""" Returns the url of the latest bhav file """
	pagehtml = urlopen("https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx").read().decode('utf-8')
	soupdata = BeautifulSoup(pagehtml, 'html.parser')
	data = list(soupdata.find_all('a', attrs = {'id': "ContentPlaceHolder1_btnhylZip"}))
	url = data[0].attrs['href']
	return url

def get_latest_data(url):
	""" Returns parsed csv data downloaded from url """
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
	
	data = [x.split(",") for x in csvdata.split('\r\n')[1:-1]]
	
	# for item in data:
	# 	print("-----------------")
	# 	print("Code: " + item[0])
	# 	print("Name: " + item[1])
	# 	print("Open: " + item[4])
	# 	print("High: " + item[5])
	# 	print("Low: " + item[6])
	# 	print("Close: " + item[7])

	return data

# get_latest_data(get_latest_url())