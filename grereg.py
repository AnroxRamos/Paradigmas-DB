import os
os.system("cls")
from flask import Flask, render_template, request
app = Flask(__name__)

# Model
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = [
    Item('Bread', 0.5),
    Item('Milk', 1.0),
    Item('Wine', 10.0)
]

# View
@app.route('/')
def index():
    return render_template('index.html', items=items)

# Controller
@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    price = float(request.form['price'])
    items.append(Item(name, price))
    return index()

if __name__ == '__main__':
    app.run(debug=True)
