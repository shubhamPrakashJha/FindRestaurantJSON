from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = 'WN0UC4JENWZZSTZROEOEJCZNLKYZO3QIEUBKA5GUDYB1IJ3U'
foursquare_client_secret = 'RT34CDWMWRZEL5DQH43P1F3A2HS0VP0OCTKRYZZFFAC2OSB0'
google_api_key = 'AIzaSyAZuiMVwYKU__4AnQ43L1B0Bgm33NSC_mw'

engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@app.route('/restaurants', methods=['GET', 'POST'])
def all_restaurants_handler():
    # return "show all restaurants"
    if request.method == 'GET':
        restaurants = session.query(Restaurant).all()
        return jsonify(Restaurant=[restaurants.serialize for restaurant in restaurants])
    else:
        return "POST request"

# YOUR CODE HERE

@app.route('/restaurants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restaurant_handler(id):
    return "get info about the particular id"

# YOUR CODE HERE

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
