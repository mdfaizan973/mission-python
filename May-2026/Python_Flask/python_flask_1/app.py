from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# import app routes
from app.routes.auth_routes import auth_bp
from app.routes.products_routes import product_bp
from app.routes.excel_products_routes import excel_products_bp

# app.register_blueprint() // inside route name
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(excel_products_bp)

if __name__ == "__main__":
    app.run(debug=True)
