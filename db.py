import redis

r = redis.Redis(host='localhost',
	port=6379, 
	password='')

def is_data_updated(date):
	last_updated = r.get('last_updated').decode('utf-8')
	if last_updated == date:
		return True
	else:
		r.set('last_updated', date)
		return False

def update_data(data):
	hash_data = {}
	os_data = {}
	for row in data:
		hash_data.update({row[1]: ','.join(row)})
		os_data.update({row[1]: row[0]})
	r.zadd('stock_ranking', os_data)
	r.hmset('stock_data', hash_data)