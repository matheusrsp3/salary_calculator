from flask import render_template

def register_routes(app):
    @app.route("/")
    def home_page():
        return render_template("index.html")


    @app.route("/sum", methods=["POST"])
    def sum_values():
        return '<h1>Route properly working...</h1>'