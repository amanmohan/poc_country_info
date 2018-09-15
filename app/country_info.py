'''
File to return country info
'''
import os
import requests

import constants as C

from utils import logger

logger = logger(os.path.basename(__file__))

def get_country_info(country_name):
    '''
    function to get country info
    Args: country_name : String
    response type: dictionary
    reponse dict Keys: C.COUNTRY_INFO_TAGS
    '''
    if not country_name:
        country_name = 'INDIA'
    #logger.info(country_name)
    country_info = {}
    # domain URL from where we get the country info
    domain_name = "https://restcountries.eu"
    uri = "/rest/v2/name/{country_name}".format(country_name=country_name)
    url = domain_name + uri
    querystring = {"fullText":"true"}
    # GET request call to get info
    try:
        logger.info(url)
        response = requests.request("GET", url, params=querystring)
    except Exception as e:
        #logger.error("Exception on Country info request - Message: {e}".format(e=e))
        return False
    if response.status_code != 200:
        return {}
    response = response.json()[0]
    for i in C.COUNTRY_INFO_TAGS:
        country_info.update({str(i): response.get(i)})
    return country_info
