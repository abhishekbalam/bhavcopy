import redis
import scrape

r = redis.Redis(host='localhost',
	port=6379, 
	password='')

def data_is_updated(date):
	last_updated = r.get('last_updated').decode('utf-8')
	if last_updated == date:
		return True
	else:
		return False

def update_data(data, date):
	r.set('last_updated', date)
	hash_data = {}
	os_data = {}
	for row in data:
		hash_data.update({row[1]: ','.join(row)})
		os_data.update({row[1]: row[0]})
	r.zadd('stock_ranking', os_data)
	r.hmset('stock_data', hash_data)

def get_top_ten():
	data = scrape.get_latest_data(scrape.get_latest_url())
	return data