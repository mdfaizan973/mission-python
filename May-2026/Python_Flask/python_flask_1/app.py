from flask import Flask
app = Flask(__name__)   

# import app routes
from app.routes.auth_routes import auth_bp
from app.routes.products_routes import product_bp

# app.register_blueprint() // inside route name
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)
