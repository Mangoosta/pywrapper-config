#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import ConfigParser
from ConfigParser import ConfigParser

"""
Nombre: pywrapper_config
Descripcion: Modulo que permite manipular archivos de configuracion.
Autor: Ernesto Crespo
Correo: ecrespo@gmail.com
Licencia: GPL Version 3
Copyright: Copyright (C) 2016 Ernesto Nadir Crespo Avila <ecrespo@gmail.com> 
Version: 0.3

"""

#Clase config
class Config(object):
    """Clase Config: facilita el uso del modulo ConfigParser"""

    def __init__(self, cnffile):
        """Constructor toma el archivo de configuracion e inicializa ConfigParser"""
        self._cnffile = cnffile
        self._config = ConfigParser()
        self._config.read(self._cnffile)

    @property
    def cnffile(self):
        """Se consulta el valor del archivo de configuracion"""
        return self._cnffile
    
    @cnffile.setter
    def cnffile(self,cnffile):
        """Se modifica el valor del archivo de configuración y se vuelve a leer el mismo"""
        self._cnffile = cnffile
        self._config.read(self._cnffile)

    def __getattr__(self):
        """__getattr__ devuelve None si se trata de acceder a un atributo que no existe"""
        return None 

    def show_sections(self):
        """Muestra las secciones del archivo de configuracion"""
        return self._config.sections()

    def show_item_section(self, section):
        """Se define la funcion que muestra los item de una seccion"""
        return self._config.items(section)

#
    def show_value_item(self, section, option):
        """Se muestra el valor de los item"""
        return self._config.get(section, option)

#
    def change(self, section, option, value):
        """Se cambia el valor de la opcion"""
        self._config.set(section, option, value)

#
    def write(self):
        """Se escribe al archivo de configuracion"""
        self._config.write(open(self._cnffile,'w'))



if __name__ == '__main__':
    #Se crea la instancia de Config pasando el archivo de configuracion ini
    configuracion = Config("./conf/androidsms.conf")
    #Se muestra las secciones
    print("Secciones: {0} ".format(configuracion.show_sections()))
    #Se muestra los items de la seccion server
    print("Items de la seccion server: {0} ".format(configuracion.show_item_section("server")))
    #Se muestra la ip de la seccion server
    print("IP: {0}".format(configuracion.show_value_item("server","ip")))
    #Se muestra el archivo de configuracion
    print("Archivo de configuracion: {0}".format(configuracion.cnffile))
    #Se cambia en caliente de archivo de configuracion
    configuracion.cnffile = "./conf/python_android_sms.conf"
    print("Archivo de configuracion: {0}".format(configuracion.cnffile))
    #Se muestra las secciones del nuevo archivo de configuracion
    print("Secciones: {0}".format(configuracion.show_sections()))

