from flask import Flask, jsonify, redirect, Response
from project.src.service import Price


def create_app():
    # Create the Flask application
    app = Flask(__name__)

    #Create an API 
    @app.route('/', methods=['GET'])
    def home():
        return Response(response="Please use the /price/ to get the price", status=200)

    @app.route('/price/',methods= ['GET'])
    def get_price():
        price = Price.fetch_price()
        if price is not None:
            return Response(response=price, status=200)
        else:
            return Response(response="Could not fetch the price", status=400)
        
    return app


