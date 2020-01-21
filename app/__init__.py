import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

class BhavCopy(object):
	@cherrypy.expose
	def index(self):
		tmpl = env.get_template('index.html')
		url = scrape.get_latest_url()
		raw_date = scrape.get_latest_date(url)

		if not db.data_is_updated(raw_date):
			raw_data = scrape.get_latest_data(url)
			db.update_data(raw_data, raw_date)

		data = db.get_top_ten()
		date = raw_date[0:2] + '/' + raw_date[2:4] + '/' + raw_date[4:6] + '20'
		# print(data[:10])

		print("Data updated at: "+date)
		return tmpl.render(tabledate=date, tabledata=data[:10])

	@cherrypy.expose
	@cherrypy.tools.json_out()
	# @cherrypy.tools.allow(methods=['POST'])
	def search(self, name):
		return db.get_stock(name)

