######
#
# File: lib/config.py
# This is the config module for handling global configurations. 
# 
######

import ConfigParser, os

def importconfig():
	""" Function call to import the config into the global stack """
	config = ConfigParser.ConfigParser()
	
	thisPath = os.path.dirname(__file__)
	parentPath = os.path.abspath(thisPath + "/..")
	
	config.read(parentPath + "/config.cfg")
	print config.sections()
	
importconfig()