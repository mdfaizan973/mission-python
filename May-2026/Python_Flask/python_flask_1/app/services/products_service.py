from app.models.products_model import create_product, delete_product, get_all_products, get_product_by_id, search_products_by_category, search_products_by_name, update_product
from uuid import uuid4

def get_all_products_services():
    result = get_all_products()
    return result

def create_products_services(data):
    
    data["id"] = str(uuid4())

    result = create_product(data)

    return {
        "message": "Product Addedd Successfully",
        "data": result
    }

def update_products_services(id, data):
    product = get_product_by_id(id)

    if product is None:
        return {
            "message": "Product not found!"
        }

    result = update_product(id, data)

    return {
        "message": "Product Updated Sccessfully!",
        "data": result
    }
    

def delete_products_services(id):
    product = get_product_by_id(id)

    if product is None:
        return {
            "message": "Product not found!"
        }

    result = delete_product(id)

    return {
        "message": "Product Deleted Successfully!",
        "data": result
    }
    

def search_products_services(name, category):

    if name not in ("", None):
        return search_products_by_name(name)

    if category not in ("", None):
        return search_products_by_category(category)

    return []

def get_product_by_id_services(id):

    result  = get_product_by_id(id)
    return result