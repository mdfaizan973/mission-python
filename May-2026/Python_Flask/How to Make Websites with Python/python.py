# import flask
from flask import Flask, redirect, url_for, render_template

# instance of the flask
app = Flask(__name__)


def isAdmin():
    return False


@app.route("/")
def home():
    return "Hello! this is the main page <h1>Hello</h1>"

# parameter route


@app.route("/<name>")
def name(name):
    return f"The page Url is: {name}!"


@app.route("/products")
def products():
    return "This is products section!"


@app.route("/users")
def users():
    return "Hello Users!"


@app.route("/not-found")
def not_found():
    return "Page not found!"


# url redirect
@app.route("/admin")
def admin():
    if isAdmin():
        return "<h2> Hello Admin </h2>"
    else:
        return redirect(url_for("not_found"))


# templete route
@app.route("/templete")
def templete_route():
    return render_template("index.html")

# templete route with parameter


@app.route("/templete-param/<name>")
def templete_with_param(name):
    return render_template(
        "index.html",
        name=name,
        name2="Faizan",
        data={"fullname": "Jhon", "age": "21"},
        list_content=["Python", "Flask", "Jinja2"]
    )


if __name__ == "__main__":
    app.run(debug=True)
