from flask import render_template, request
from babel.numbers import format_currency, parse_decimal

def register_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/calculate", methods=["POST"])
    def calculate():
        # Collecting POST data
        base_salary = request.form.get("base_salary")
        percentage_advance = request.form.get("percentage_advance") 

        # Conventing data for calculate
        base_salary = float(parse_decimal(base_salary, locale="pt_BR")) # Float
        percentage_advance = int(percentage_advance) # Int

        # Calculating
        advance_payment_result = base_salary * (percentage_advance / 100)
        
        # Formatting results
        formatted_advance_payment = format_currency(advance_payment_result, "BRL", locale="pt_BR")

        # Packaging values
        formatted_values = {
            "formatted_advance_payment": formatted_advance_payment,
        }

        return render_template("result.html", **formatted_values)