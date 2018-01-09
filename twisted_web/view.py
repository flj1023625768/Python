#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from twisted.web.template import Element, renderer, XMLFile, flattenString
from twisted.python.filepath import FilePath
import model
class View(Element):
  loader = XMLFile(FilePath('view.xml'))
  @renderer
  def title(self, request, tag):
    return tag(model.title)
  @renderer
  def person(self, request, tag):
    for p in model.persons:
      yield tag.clone().fillSlots(avatar=p[1],nick=p[0])

#def renderDone(o):
#  print(o)
#flattenString(None, View()).addCallback(renderDone)

