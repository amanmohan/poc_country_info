import pygeoip
import os

import constants as C

from utils import logger

def country_locator_with_ip(ip):
	'''
	Function to return country name with ip
	Args: ip : String
	Returns : country name: String
	'''
	gi = pygeoip.GeoIP(C.GEO_DATA_FILE)
	try:
		country_name = gi.country_code_by_addr(ip)
	except Exception as e:
		logger.error("Exception retriving country name - Message: {e}".format(e=e))
	return country_name
