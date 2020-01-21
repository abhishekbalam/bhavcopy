import redis

r = redis.Redis(host='localhost',
	port=6379, 
	password='')

def data_is_updated(date):

	if r.exists('last_updated'):
		last_updated = r.get('last_updated').decode('utf-8')
		return True if last_updated == date else False
	else:
		return False

def update_data(data, date):
	r.set('last_updated', date)
	
	hash_data = {}
	os_data = {}

	try:
		with r.pipeline() as pipe:
			for row in data:
				stock = {
					'name': row[1],
					'open': row[2],
					'high': row[3],
					'low': row[4],
					'close': row[5]
				}
				pipe.hmset('stock:'+row[0], stock)
				pipe.zadd('stock_ranking', { row[1]: int(row[0]) })
			pipe.execute()
		return True
	except:
		return False

def get_top_ten():
	
	hashes = r.zrange('stock_ranking', 0 , 10, withscores=True)
	data = []
	for name, code in hashes:
		stock = r.hgetall('stock:' + str(int(code)))
		stock = { x.decode('utf-8'): stock.get(x).decode('utf-8') for x in stock.keys() } 

		# print(stock)
		stock.update({ 'code': str(int(code)) })
		data.append(stock)
	return data

def get_stock(name):
	stock_code = r.zscore('stock_ranking', name)
	stock = {}
	if stock_code is None:
		stock.update({ 'status': False})
	else:
		stock_code = str(int(stock_code))
		stock.update(r.hgetall('stock:'+ stock_code))
		stock = { x.decode('utf-8'): stock.get(x).decode('utf-8') for x in stock.keys() } 
		stock.update({ 'code': stock_code})
		stock.update({ 'status': True})
	return stock

