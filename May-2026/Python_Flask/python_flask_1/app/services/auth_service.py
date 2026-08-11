from app.models.auth_model import add_user, delete_user, get_all_users, update_user, user_find_by_id
from app.models.json_model import write_data, read_data
from uuid import uuid4
import pandas as pd

def get_all_users_services():
    result = get_all_users()
    return result

def get_single_user_services(id):
    user = user_find_by_id(id)
    return user

def create_users_services(new_user):

    new_user["id"] = str(uuid4())
    created_user = add_user(new_user)

    return {
        "message": "User Added Successfully!",
        "user": created_user
    }


def update_user_services(id, updated_user):
    user = user_find_by_id(id)

    if user is None:
        return {
            "message": "User not found."
        }, 404

    update_user(id, updated_user)

    return {
        "message": "User updated Successfully!",
        "user id": id
    }


def delete_user_services(id):
    user = user_find_by_id(id)

    if user is None:
        return {
            "message": "User not found."
        }, 404

    delete_user(id)

    return {
        "message": "User Deleted successfully",
        "user-id": id
    }

def excel_file_upload_services(excel_file, title, description):

    db_data = read_data()

    if not excel_file:
        return {"message": "No file uploaded"}

    df = pd.read_excel(excel_file)
    res = df.to_dict(orient="records")

    print(res)

    if db_data["products"]:
        db_data["products"].extend(res)
    else:
        db_data["products"] = res   
    write_data(db_data)

    return {"data": "res", "title": title, "description": description}