import os
import cherrypy

class BhavCopy(object):
	@cherrypy.expose
	def index(self):
		return "Hello World"

	@cherrypy.expose
	@cherrypy.tools.json_out()
	# @cherrypy.tools.allow(methods=['POST'])
	def search(self, name):
		return {'Name': name}

if __name__ == '__main__':
	conf = {
		'/': {
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './static'
		}
	}
	cherrypy.quickstart(BhavCopy(), '/', conf)