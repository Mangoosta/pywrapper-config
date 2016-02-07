# pywrapper-config
Wrapper to ConfigParser  python module



How to use pywraper-config:
```
import pywrapper_config


config = pywrapper_config.Config("./conf/tests.conf")
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

```