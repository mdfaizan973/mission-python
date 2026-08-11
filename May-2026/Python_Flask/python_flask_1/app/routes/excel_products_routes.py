from flask import Blueprint, jsonify, request
from app.services.excel_products_service import create_excel_products_service, get_excel_products_services

excel_products_bp = Blueprint("excel_products", __name__)

@excel_products_bp.route("/excel_products", methods=["POST"])
def create_excel_products():
    excel_file = request.files.get("excel_file")
    result = create_excel_products_service(excel_file)
    return jsonify(result)

@excel_products_bp.route("/excel_products", methods=["GET"])
def get_excel_products():
    result  = get_excel_products_services()
    return jsonify(result)