#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import ConfigParser
from ConfigParser import ConfigParser
from json import dumps

"""
Name: pywrapper_config
Description: Wrapper to ConfigParser
Author: Ernesto Crespo
Email: ecrespo@gmail.com
License: GPLv3
Copyright: Copyright (C) 2016 Ernesto Nadir Crespo Avila <ecrespo@gmail.com>
Version: 0.3.2

"""


class Config(object):
    """Config Class to manipulate a config file"""

    def __init__(self, cnffile):
        """Set atributes"""
        self._cnffile = cnffile
        self._config = ConfigParser()
        self._config.read(self._cnffile)

    @property
    def cnffile(self):
        """return  config file value"""
        return self._cnffile

    @cnffile.setter
    def cnffile(self,cnffile):
        """change config file attribute"""
        self._cnffile = cnffile
        self._config.read(self._cnffile)

    @cnffile.deleter
    def cnffile(self):
        """Delete config file variable"""
        print ("Config file variable and config instance Deleted")
        self._cnffile = None
        self._config = None

    def __getattr__(self):
        """None returned when you query a value that does not exist"""
        return None

    def show_sections(self):
        """Show sections"""
        return self._config.sections

    def show_sectionsDict(self):
        """return Sections in dictionary"""
        return {'sections': self._config.sections()}

    def show_sectionsJSON(self):
        """Show sections in json format"""
        return dumps(self.show_sectionsDict())

    def show_item_section(self, section):
        """Show items from section"""
        return self._config.items(section)

    def show_item_sectionDict(self, section):
        """Show items from section in dictionary"""
        elements = {}
        for element in self._config.items(section):
            elements[element[0]] =  element[1][1:-1]
        return {'section': section, 'items': elements}

    def show_item_sectionJSON(self,section):
        """Show items from section in a json format"""
        return dumps(self.show_item_sectionDict(section))

#
    def show_value_item(self, section, option):
        """Show item value"""
        return self._config.get(section, option)

    def show_value_itemDict(self, section, option):
        """Show item value in dictionary format """
        return {'section':section,'option': {option: self._config.get(section, option)[1:-1]}}

    def show_value_itemJSON(self, section, option):
        """Show item value in json format """
        return dumps(self.show_value_itemDict(section,option))

#
    def change(self, section, option, value):
        """Change option value"""
        self._config.set(section, option, value)

#
    def write(self):
        """Write config file"""
        self._config.write(open(self._cnffile,'w'))
