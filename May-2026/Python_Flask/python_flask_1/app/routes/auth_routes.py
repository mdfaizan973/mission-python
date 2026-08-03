from flask import Blueprint, request, jsonify
from app.services.auth_service import create_users_services, delete_user_services, get_all_users_services, get_single_user_services, update_user_services

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/users", methods=["GET"])
def get_users():

    users_list = get_all_users_services()
    return jsonify(users_list)


@auth_bp.route("/users", methods=["POST"])
def create_user():
    print("Route Called")
    new_user = request.get_json()

    result = create_users_services(new_user)

    return jsonify(result)


@auth_bp.route("/users/<id>", methods=["PATCH", "PUT"])
def update_user(id):

    updated_user = request.get_json()

    result = update_user_services(id, updated_user)

    return jsonify(result)


@auth_bp.route("/users/<id>", methods=["DELETE"])
def delete_user(id):

    result  = delete_user_services(id)

    return jsonify(result)


@auth_bp.route("/users/<id>", methods=["GET"])
def get_single_user(id):

    result = get_single_user_services(id) 

    return jsonify(result)