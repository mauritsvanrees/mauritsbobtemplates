# -*- coding: utf-8 -*-


class RegEntry(object):
    def __init__(self):
        self.template = ""
        self.plonecli_alias = ""
        self.depend_on = None
        self.deprecated = False
        self.info = ""


def maurits_plone_addon():
    reg = RegEntry()
    reg.template = "mauritsbobtemplates:addon"
    reg.plonecli_alias = "maurits_plone_addon"
    return reg


def maurits_plone_buildout():
    reg = RegEntry()
    reg.template = "mauritsbobtemplates:buildout"
    reg.plonecli_alias = "maurits_buildout"
    return reg
