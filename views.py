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
    if request.method == 'GET':
        restaurants = session.query(Restaurant).all()
        return jsonify(
            restaurants=[restaurant.serialize for restaurant in restaurants])
    elif request.method == 'POST':
        # get location and meal type from query
        location = request.args.get('location')
        mealType = request.args.get('mealType')
        # find restaurant based on location and meal Type
        restaurantInfo = findARestaurant(mealType, location)
        if restaurantInfo != "No Restaurants Found":
            # add this new restaurant in database
            restaurant = Restaurant(restaurant_name=unicode(restaurantInfo['name']),
                                    restaurant_address=unicode(restaurantInfo['address']),
                                    restaurant_image=restaurantInfo['image'])
            session.add(restaurant)
            session.commit()
            # return json object
            return jsonify(restaurant = restaurant.serialize)

    # return "show all restaurants"
    else:
        return jsonify({"error": "No restaurant found"})


# YOUR CODE HERE

@app.route('/restaurants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restaurant_handler(id):
    return "get info about the particular id"

# YOUR CODE HERE

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
