# 🧩 1. Basic Setup
from flask import Flask, jsonify, request
import json

# Flask → main class to create app
# jsonify → convert Python → JSON response
# request → get data from frontend (POST/PUT)
# json → read/write JSON file

# 🧩 2. Create App Object
app = Flask(__name__)

# __name__ → tells Flask this file is main app

# 🧩 3. Helper Functions (Read & Write JSON)


def read_data():
    with open("data.json", "r") as file:
        return json.load(file)

# with open() → safely open file
# "r" → read mode
# json.load() → convert JSON file → Python list


def write_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# "w" → write mode
# json.dump() → Python list → JSON file
# indent=4 → makes JSON readable


# 🟢 CRUD OPERATIONS

# 📌 1. READ ALL DATA (GET)

@app.route("/users", methods=["GET"])
def get_user():
    users_list = read_data()["users"]
    return jsonify(users_list)


# @app.route → creates API endpoint
# GET → fetch data
# jsonify() → return JSON response


# 📌 2. CREATE USER (POST)

@app.route("/users", methods=["POST"])
def add_user():

    data = read_data()

    new_user = request.get_json()   # Get JSON data from FE / get_json given by flask

    new_user["id"] = len(data["users"]) + 1

    data["users"].append(new_user)   # Add new user into users list

    write_data(data)   # Save updated data back into data.json file

    return jsonify({
        "message": "User added successfully",
        "user": new_user
    })


# 📌 3. UPDATE USER (PUT)

# route <int:id> with id method
# api funtion
# get full users data
# get the newly record
# run a loop and match the id
# if matched, update user[id] with updated_user from request.get_json()
# updated data into the users data list
# call write function with full data
# return jsonify({"message": "", "updated_user": updated_data})

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):

    data = read_data()

    updated_user = request.get_json()

    for user in data["users"]:
        if user["id"] == id:
            updated_user["id"] = id

            user.clear()   # remove old user data
            user.update(updated_user)   # replace with updated user data

            write_data(data)

            return jsonify({
                "message": "User updated successfully",
                "user-id": id
            })


# 📌 4. DELETE USER (DELETE)

# route with DELETE method and id parameter
# get full users data
# run loop through users list
# match current user id with URL id
# if matched:
    # use remove() function to delete user from list
# call write function with updated full data
# return jsonify success response
# if no user matched:
    # return user not found response

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_users(id):
    data = read_data()

    for user in data["users"]:
        if user["id"] == id:

            data["users"].remove(user)

            write_data(data)

            return jsonify({
                "message": "User Deleted successfully",
                "user-id": id
            })

    return jsonify({
        "message": "User Deleted successfully",
        "user-id": id
    })


# 🚀 5: Run Flask App
if __name__ == "__main__":
    app.run(debug=True)

# __main__ → runs only when file executed directly
# debug=True → auto restart server when code changes
