import os
import cherrypy
from jinja2 import Environment, FileSystemLoader
import scrape, db

env = Environment(loader=FileSystemLoader('templates'))

class BhavCopy(object):
	@cherrypy.expose
	def index(self):
		tmpl = env.get_template('index.html')
		url = scrape.get_latest_url()
		date = scrape.get_latest_date(url)

		if db.data_is_updated(date):
			data = db.get_top_ten()
		else:
			data = scrape.get_latest_data(url)
			db.update_data(data, date)
		return tmpl.render(date='20/1/2020', tabledata=data[1:10])

	@cherrypy.expose
	@cherrypy.tools.json_out()
	# @cherrypy.tools.allow(methods=['POST'])
	def search(self, name):
		return {'Name': name}

if __name__ == '__main__':
	conf = {
		'/': {
			'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
		},
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
		}
	}
	cherrypy.quickstart(BhavCopy(), '/', conf)