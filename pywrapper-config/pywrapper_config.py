#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import ConfigParser
from ConfigParser import ConfigParser

"""
Name: pywrapper_config
Description: Wrapper to ConfigParser python module
Author: Ernesto Crespo
Email: ecrespo@gmail.com
License: GPLv3
Copyright: Copyright (C) 2016 Ernesto Nadir Crespo Avila <ecrespo@gmail.com> 
Version: 0.3

"""

#Clase config
class Config(object):
    """Config Class to manipulate a config file"""

    def __init__(self, cnffile):
        """Set atributes"""
        self._cnffile = cnffile
        self._config = ConfigParser()
        self._config.read(self._cnffile)

    @property
    def cnffile(self):
        """Search config file value"""
        return self._cnffile
    
    @cnffile.setter
    def cnffile(self,cnffile):
        """change config file attribute"""
        self._cnffile = cnffile
        self._config.read(self._cnffile)

    def __getattr__(self):
        """None returned when you query a value that does not exist"""
        return None 

    def show_sections(self):
        """Show sections"""
        return self._config.sections()

    def show_item_section(self, section):
        """Show items from section"""
        return self._config.items(section)

#
    def show_value_item(self, section, option):
        """Show item value"""
        return self._config.get(section, option)

#
    def change(self, section, option, value):
        """Change option value"""
        self._config.set(section, option, value)

#
    def write(self):
        """Write config file"""
        self._config.write(open(self._cnffile,'w'))



if __name__ == '__main__':
    config = Config("./conf/tests.conf")
    #Show sections 
    print("Sections: {0} ".format(config.show_sections()))
    #Show server section
    print("Items server section: {0} ".format(config.show_item_section("server")))
    #Show ip server
    print("IP: {0}".format(config.show_value_item("server","ip")))
    #Show config file
    print("Config file: {0}".format(config.cnffile))
    #Change config file
    config.cnffile = "./conf/tests2.py"
    print("Config file: {0}".format(config.cnffile))
    #Show sections from new config file 
    print("Secciones: {0}".format(config.show_sections()))

