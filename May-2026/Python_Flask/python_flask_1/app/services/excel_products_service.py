from app.models.json_model import read_data, write_data
import pandas as pd
from uuid import uuid4

def create_excel_products_service(excel_file):

    db_data = read_data()

    if not excel_file:
        return {"message": "Excel File not found!"}
    
    df = pd.read_excel(excel_file)
    
    res = df.to_dict(orient="records")

    for item in res:
        item["product_uuid"] = str(uuid4())
    
    if db_data["excel_data"]:
        db_data["excel_data"].extend(res)
    else:
        db_data["excel_data"] = res

    write_data(db_data)

    return {"message": "Product Added Successfully!", "data": res}

def get_excel_products_services():
    db_data = read_data()
    data = db_data["excel_data"]
    return data