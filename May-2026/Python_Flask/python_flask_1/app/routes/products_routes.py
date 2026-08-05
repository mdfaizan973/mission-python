from unittest import result
from flask import Blueprint, jsonify, request
from app.services.products_service import create_products_services, delete_products_services, get_all_products_services, search_products_services, update_products_services

product_bp = Blueprint("products", __name__)

# GET
@product_bp.route("/products", methods=["GET"])
def get_products():

    result = get_all_products_services()
    return jsonify(result)

# POST
@product_bp.route("/products", methods=["POST"])
def create_products():
    product = request.get_json()

    result = create_products_services(product)
    return jsonify(result)

# PATCH/PUT
@product_bp.route("/products/<id>", methods=["PUT", "PATCH"])
def update_products(id):
    product = request.get_json()

    result  = update_products_services(id, product)
    return jsonify(result)

# DELETE
@product_bp.route("/products/<id>", methods=["DELETE"])
def delete_products(id):

    result = delete_products_services(id)
    return jsonify(result)

# Search Product : GET /products/search?name=apple ⭐
@product_bp.route("/products/search", methods=["GET"])
def search_products():
    name = request.args.get("name")
    category = request.args.get("category")

    result = search_products_services(name, category)

    return jsonify(result)

# Get Product by ID : GET /products/3
# Delete All Products : DELETE /products
# Filter by Price: GET /products/filter?min=50&max=100
# Sort Products: GET /products/sort/asc : GET /products/sort/desc
# Count Products : GET /products/categories
# Most Expensive, Cheapest and Average Product : GET /products/price<type> max, min, avg
