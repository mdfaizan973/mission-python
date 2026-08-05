from app.models.json_model import read_data, write_data

def get_all_products():
    result = read_data()["products"]
    return result


def create_product(data):
    db_data = read_data()

    db_data["products"].append(data)

    write_data(db_data)

    return data

def get_product_by_id(id):
    db_products = read_data()["products"]

    for product in db_products:
        if product["id"] == id:
            return product
    
    return None

def update_product(id, data):
    db_prdoduct = read_data()

    for product in db_prdoduct["products"]:
        if product["id"] == id:

            product.update(data)

            write_data(db_prdoduct)

    return id

def delete_product(id):
    db_product = read_data()

    for product in db_product["products"]:
        if product["id"] == id:
            db_product["products"].remove(product)

            write_data(db_product)

    return id


def search_products_by_name(name):
    db_product = read_data()["products"]

    result = filter(lambda product: product["name"].lower() == name.lower(), db_product)
    return list(result)
        

def search_products_by_category(category):
    db_product = read_data()["products"]

    result = filter(lambda product : product["category"].lower() == category.lower() , db_product)
    return list(result)