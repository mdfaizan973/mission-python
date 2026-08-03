from app.models.json_model import read_data, write_data

def get_all_users():
    db_data = read_data()
    return db_data["users"]

def add_user(data):
    db_data = read_data()
    db_data["users"].append(data)

    write_data(db_data)

    return data


def user_find_by_id(id):
    db_data = read_data()["users"]

    for user in db_data:
        if user["id"] == id:
            return user
    
    return None


def update_user(id, data):
    db_data = read_data()

    for user in db_data["users"]:
        if user["id"] == id:
            user.update(data)

            write_data(db_data)

    return data
    

def delete_user(id):
    db_data = read_data()

    for user in db_data["users"]:
        if user["id"] == id:
            db_data["users"].remove(user)

            write_data(db_data)

    return id