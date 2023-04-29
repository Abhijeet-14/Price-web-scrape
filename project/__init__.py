from flask import Flask, jsonify
from project.src.service import Price


def create_app():
    # Create the Flask application
    app = Flask(__name__)

    #Create an API 
    # @app.route('/price', methods=['GET'])
    # def get_price():
    #     price = Price.fetch_price()
    #     if price is not None:
    #         return price
    #     else:
    #         return "Could not fetch the price"
        
    @app.route('/',methods= ['GET'])
    def home():
        return 'Please use the "URL/price" to get the price'
        
    return app


