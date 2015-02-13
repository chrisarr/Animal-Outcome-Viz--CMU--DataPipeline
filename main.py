#!/usr/bin/env python
from google.appengine._internal.django.utils.simplejson import JSONEncoder
from jinja2 import TemplateNotFound
import os

import webapp2
from webapp2_extras import jinja2
from webapp2_extras import json
import logging
import httplib2
from apiclient.discovery import build
import urllib
import json

import numpy as np
from numpy import *

from django.utils import simplejson

API_KEY = "AIzaSyDfn6Fn3TQylyqqNxPVx2_tZkXDwQiXGLw"
TABLE_ID = "1ZzG05-qoaEBiSOjP0Wbrm_wnaLAMdQuZBNv_Zgtt"


# BaseHandler subclasses RequestHandler so that we can use jinja
class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

        # This will call self.response.write using the specified template and context.
        # The first argument should be a string naming the template file to be used. 
        # The second argument should be a pointer to an array of context variables
        #  that can be used for substitutions within the template
    def render_response(self, _template, context):
        values = {'url_for': self.uri_for}
        #logging.info(context)
        values.update(context)
        self.response.headers['Content-Type'] = 'text/html'

        try:
            # Renders a template and writes the result to the response.
            rv = self.jinja2.render_template(_template, **values)
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write(rv)

        except TemplateNotFound:
            self.abort(404)


# Class MainHandler now subclasses BaseHandler instead of webapp2
class MainHandler(BaseHandler):
    # This method should return the html to be displayed
    def get(self):

        dates = {'2011-01', '2011-02', '2011-03', '2011-04', '2011-05', '2011-06', '2011-07', '2011-08', '2011-09', '2011-10', '2011-11', '2011-12', '2012-01', '2012-02', '2012-03', '2012-04', '2012-05', '2012-06', '2012-07', '2012-08', '2012-09', '2012-10'}

        # add it to the context being passed to jinja
        variables = {'x_labels':dates}

        # and render the response
        self.render_response('index.html', variables)


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)