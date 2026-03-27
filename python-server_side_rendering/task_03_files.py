from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)


@app.route('/products')
def products_display():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        products = read_json_file('./products.json')
    elif source == 'csv':
        products = read_csv_file('./products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    if id:
        products = [product for product in products if product['id'] == id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def read_csv_file(file_path):
    with open(file_path, 'r') as f:
        return list(csv.DictReader(f))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
