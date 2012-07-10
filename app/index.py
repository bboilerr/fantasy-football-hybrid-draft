import os
import sys
import logging
import urllib
import webapp2

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class MainPage(webapp2.RequestHandler):
  def get(self):
    template = env.get_template('index.html')

    self.response.out.write(
            template.render(
                var='World'
                )
            )

app = webapp2.WSGIApplication([('/', MainPage)])
