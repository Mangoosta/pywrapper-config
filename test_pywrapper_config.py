#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywrapper_config import Config



config = Config("./conf-examples/tests.conf")

print (config.show_sections())
print (config.show_sectionsJSON())
print (config.show_item_section('server'))
print (config.show_item_sectionJSON('server'))
print (config.show_value_item('server','ip'))
print (config.show_value_itemJSON('server','ip'))
