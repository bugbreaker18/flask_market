from flask import Flask, render_template, request
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    item_details = [
        {
            "id" : 1, "name" : "VR Glasses", "barcode" : 9999988888, "price" : 500
        },
        {
            "id" : 2, "name" : "Z-fold", "barcode" : 8888899999, "price" : 400
        },
        {
            "id" : 2, "name" : "Alienware", "barcode" : 7777788888, "price" : 900
        }
    ]
    return render_template('market.html', items = item_details)
