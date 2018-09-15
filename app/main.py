import os

import constants as C

from datetime import timedelta

from flask import Flask, session, render_template, request

from utils import logger
from ip_locator import country_locator_with_ip
from country_info import get_country_info

logger = logger(os.path.basename(__file__))

#Flask Server
app = Flask(__name__)
app.secret_key = C.SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def register():
        if request.method == 'GET':
                logger.info("User on the Page")
                user_ip_address = request.access_route[0]
                logger.info(user_ip_address)
                user_country = country_locator_with_ip(ip=user_ip_address)
        if request.method == 'POST':
                logger.info("User Made a post request")
                user_country = request.form.get('name').upper()
        country_info = get_country_info(country_name=user_country)
        logger.info(country_info)
        return render_template('index.html', country_info=country_info)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0',
          port=5000)
