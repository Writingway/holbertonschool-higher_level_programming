from flask import Flask, json, render_template, request
import csv
import sqlite3

app = Flask(__name__)


@app.route('/products')
def products_display():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        products = read_json_file('./products.json')
    elif source == 'csv':
        products = read_csv_file('./products.csv')
    elif source == 'sql':
        products = read_sql_file('./products.db')
    else:
        return render_template('product_display.html', error="Wrong source")

    if id:
        try:
            id = int(id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")
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


def read_sql_file(file_path):
    file_path = file_path.replace('./', '')
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    conn.close()
    return products


if __name__ == '__main__':
    app.run(debug=True, port=5000)
