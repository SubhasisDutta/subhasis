import webapp2
import os
from google.appengine.ext.webapp import template


class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="text/html"
        template_values = {}
        path=os.path.join(os.path.dirname(__file__),'../../template/index.html')
        page=template.render(path,template_values) 
        self.response.out.write(page)
