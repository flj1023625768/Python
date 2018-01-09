#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from view import View
from twisted.web import server, resource
from twisted.internet import reactor, endpoints
from twisted.web.template import Element, flattenString
class Foo(resource.Resource):
  isLeaf = True  
  def __init__(self):
    self.html = ''
  def renderDone(self, html):
    self.html = html
    print self.html
  def render_GET(self, request):
    flattenString(None, View()).addCallback(self.renderDone)
    print self.html
    return self.html
site = server.Site(Foo())
endpoint = endpoints.TCP4ServerEndpoint(reactor, 9511)
endpoint.listen(site)
reactor.run()

