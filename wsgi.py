import cherrypy
import os
from app import BhavCopy, scrape, db

# This file is just to be a launch point to 
# the application
app = cherrypy.tree.mount(BhavCopy(), '/')

if __name__=='__main__':
	cherrypy.config.update({
		'server.socket_host': '127.0.0.1',
		'server.socket_port': 8085,
	})
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