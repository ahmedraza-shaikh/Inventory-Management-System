from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import add_product, get_all_products, delete_product, update_product, search_product, low_stock_products

app = Flask(__name__)

# ── Homepage ──
@app.route("/")
def index():
    products = get_all_products()
    low_stock = low_stock_products()
    return render_template("index.html", 
                         products=products, 
                         low_stock=low_stock)

# ── Add Product ──
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    category = request.form["category"]
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])
    add_product(name, category, quantity, price)
    return redirect(url_for("index"))

# ── Delete Product ──
@app.route("/delete/<int:id>")
def delete(id):
    delete_product(id)
    return redirect(url_for("index"))

# ── Update Product ──
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    category = request.form["category"]
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])
    update_product(id, name, category, quantity, price)
    return redirect(url_for("index"))

# ── Search Product ──
@app.route("/search")
def search():
    keyword = request.args.get("keyword", "")
    products = search_product(keyword)
    low_stock = low_stock_products()
    return render_template("index.html",
                         products=products,
                         low_stock=low_stock,
                         keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)