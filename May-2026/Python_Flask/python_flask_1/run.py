from flask import Flask, jsonify, request
import json
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from uuid import uuid4

from utils import check_password

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "faizan123"
jwt = JWTManager(app)

def read_data():
    with open("data.json", "r") as file:
        return json.load(file)


def write_data(data):
    with open("data.json", "w") as file:
        return json.dump(data, file, indent=4)


@app.route("/")
def hello_world():
    return jsonify("Hello Python")


@app.route("/users", methods=["GET"])
def get_usres():
    users_list = read_data()["users"]
    return jsonify(users_list)


# take the data from client
# convert the data into Python dictionary -> request.get_json()
# add into write data function
@app.route("/users", methods=["POST"])
def create_user():

    data = read_data()

    new_user = request.get_json()

    new_user["id"] = len(data["users"])+1

    data["users"].append(new_user)

    write_data(data)

    return jsonify({
        "message": "User Added Successfully!",
        "user": new_user
    })


# Update Users By id
# api end point
# function that takes id
# get the full list
# update the record of given id
# write data
@app.route("/users/<int:id>", methods=["PATCH", "PUT"])
def update_user(id):

    data = read_data()

    updated_user = request.get_json()

    for user in data["users"]:
        if user["id"] == id:
            updated_user["id"] = id

            # user.clear()
            user.update(updated_user)

            write_data(data)

            return jsonify({
                "message": "User updated Successfully!",
                "user id": id
            })

    return jsonify({
        "message": "User not found!",
        "user id": id
    })


# Delete users By id
# api end point
# function that takes id
# get the full list
# remove the record of given id
# write data

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    data = read_data()

    for user in data["users"]:
        if user["id"] == id:

            data["users"].remove(user)
            write_data(data)

            return jsonify({
                "message": "User Deleted successfully",
                "user-id": id
            })
        else:
            return jsonify({
                "message": "User not found!",
                "user id": id
            })
# -----------------------------------------------------------------

# Authentication Api's

# Register
@app.route("/register", methods=["POST"])
def register(): 
    request_data = request.get_json()
    data = read_data()

    request_email = request_data.get("email")
    request_password = request_data.get("password")
    
    for user in data["users"]:
        if request_email == user["email"]:
            return({
                "message": "Email already exists"
            }), 409

    result = check_password(request_password)

    if not result["status"]:
        return jsonify({
            "message": result["message"]
        }), 400
  
    request_data["id"] = str(uuid4())
    data["users"].append(request_data)
    write_data(data)


    return jsonify({
        "message": "User Registration Successfully!"
    }), 200

# Login
@app.route("/login",  methods=["POST"])
def login():
    request_data = request.get_json()
    data = read_data()

    email = request_data.get("email")
    password = request_data.get("password")

    if email in (None, "") or password in (None, ""):
        return jsonify({
            "message": "Email and password are required."
        }), 400

    user = None

    for item in data["users"]:
        if item["email"] == email:
            user = item
            break

    if user is None:
        return jsonify({
            "message": "User not found."
        }), 404

    result = check_password(password)

    if not result["status"]:
        return jsonify({
            "message": result["message"]
        }), 400

    if password != user["password"]:
        return jsonify({
            "message": "Wrong credentials."
        }), 401

    access_token = create_access_token(identity=user["id"])

    return jsonify({
        "message": "Login successful.",
        # "data": user,
        "access_token": access_token
    }), 200



# Products Api's

# GET

@app.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    userId = get_jwt_identity()
    products_list = read_data()["products"]

    return jsonify({
        "data": products_list,
        "user": userId
    })


# POST
@app.route("/products", methods=["POST"])
def create_products():
    data = read_data()

    new_product = request.get_json()
    new_product["id"] = len(data["products"])+1

    data["products"].append(new_product)

    write_data(data)

    return jsonify({
        "message": "Product Added Successfully!",
        "product": new_product
    })


# PUT | PATCH
@app.route("/products/<int:id>", methods=["PUT", "PATCH"])
def update_product(id):
    data = read_data()
    updated_prod = request.get_json()

    for prod in data["products"]:
        print("Checking:", prod["id"])
        if prod["id"] == id:

            updated_prod["id"] = id
            prod.update(updated_prod)

            write_data(data)

            return jsonify({
                "message": "Product Updated Successfully!",
                "id": id
            })

    return jsonify({
        "message": "Product Not Found!",
        "id": id
    })


# DELETE
@app.route("/products/<int:id>", methods=["DELETE"])
def delete_products(id):
    data = read_data()

    for prod in data["products"]:
        if prod["id"] == id:
            data["products"].remove(prod)

            write_data(data)

            return jsonify({
                "message": "Product Deleted Successfully!",
                "id": id
            })

    return jsonify({
        "message": "Product not found!",
        "id": id
    })


# Get Product by ID : GET /products/3
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    data = read_data()

    for prod in data["products"]:
        if prod["id"] == id:
            return jsonify(prod)

    return jsonify({
        "message": "Product Not Found!",
        "user-id": id
    }), 404


# Search Product : GET /products/search?name=apple
@app.route("/products/search", methods=["GET"])
def search_products():
    name = request.args.get("name")
    category = request.args.get("category")

    data = read_data()["products"]

    filtered_list = []

    if name not in (None, ""):
        filtered_list = filter(
            lambda product: product["name"].lower() == name.lower(), data)

    elif category not in (None, ""):
        filtered_list = filter(
            lambda product: product["category"].lower() == category.lower(), data)

    else:
        filtered_list = data

    result = list(filtered_list)

    return jsonify(result)


# Filter by Price: GET /products/filter?min=50&max=100
@app.route("/products/filter", methods=["GET"])
def price_range_filter():
    minimum = request.args.get("min")
    maximum = request.args.get("max")

    has_minimum = minimum not in (None, "")
    has_maximum = maximum not in (None, "")

    data = read_data()["products"]
    filtered_list = []

    if minimum in (None, "") and maximum in (None, ""):
        return jsonify({
            "message": "Provide at least one query parameter: min or max."
        }), 400

    try:
        if has_minimum:
            minimum = int(minimum)

        if has_maximum:
            maximum = int(maximum)

        if has_minimum and has_maximum:
            if minimum > maximum:
                return jsonify(filtered_list)

    except ValueError:
        return jsonify({
            "message": "min and max must be valid integers"
        }), 400

    if has_minimum and has_maximum:
        filtered_list = list(filter(
            lambda product: product["price"] >= minimum and product["price"] <= maximum, data))

    elif has_minimum:
        filtered_list = list(
            filter(lambda product: product["price"] >= minimum, data))

    elif has_maximum:
        filtered_list = list(
            filter(lambda product: product["price"] <= maximum, data))

    return jsonify(filtered_list)

# Sort Products: GET /products/sort/asc : GET /products/sort/desc


@app.route("/products/sort/<order>", methods=["GET"])
def sort_products(order):
    sort_by = order.lower()
    data = read_data()["products"]

    if sort_by not in ("asc", "desc"):
        return jsonify({
            "message": "Invalid sort order. Use 'asc' or 'desc'."
        }), 400

    sorted_list = []

    if sort_by == "asc":
        sorted_list = sorted(data, key=lambda item: item["price"])
    elif sort_by == "desc":
        sorted_list = sorted(
            data, key=lambda item: item["price"], reverse=True)

    return jsonify(sorted_list)


# Count Products : GET /products/categories
@app.route("/products/categories", methods=["GET"])
def procucts_count():
    data = read_data()["products"]

    result = {}

    for product in data:
        cat = product["category"]

        if cat not in result:
            result[cat] = {"data": [], "count": 0}

        result[cat]["data"].append(product)
        # result[cat]["count"] = len(result[cat]["data"])
        result[cat]["count"] += 1

    result["total_count"] = len(data)
    return jsonify(result)


# Most Expensive, Cheapest and Average Product : GET /products/price<type> max, min, avg
@app.route("/products/price/<price_filter>", methods=["GET"])
def product_by_price_type(price_filter):
    price_type = price_filter.lower()
    data = read_data()["products"]

    if price_type not in ("max", "min", "avg"):
        return jsonify({
            "message": "There are no products to calculate the requested price."
        }), 400

    if len(data) == 0:
        return jsonify([])

    result_data = []

    if price_type == "min":
        result_data = min(data, key=lambda item: item["price"])

    elif price_type == "max":
        result_data = max(data, key=lambda item: item["price"])

    elif price_type == "avg":
        total_sum = sum(product["price"] for product in data)
        total_products = len(data)
        result_data = {
            "id": "-",
            "name": "-",
            "price": total_sum / total_products,
            "category": "-"
        }

    return jsonify(result_data)


# Delete All Products : DELETE /products
@app.route("/products", methods=["DELETE"])
def delete_all():

    data = read_data()
    total_count = len(data["products"])
    data["products"].clear()
    write_data(data)

    return jsonify({"message": f"All products have been deleted. {total_count} data affected "})


if __name__ == "__main__":
    app.run(debug=True)
