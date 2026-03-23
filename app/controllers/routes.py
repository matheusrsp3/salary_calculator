from flask import render_template, request
from babel.numbers import format_currency, parse_decimal
from app.utils import get_divider

def register_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/calculate", methods=["POST"])
    def calculate():
        # Collecting POST data
        base_salary = request.form.get("base_salary")
        percentage_advance = request.form.get("percentage_advance") 
        hours_worked_per_week = request.form.get("hours_worked_per_week")

        # Conventing data for calculate
        base_salary = float(parse_decimal(base_salary, locale="pt_BR")) # Float
        percentage_advance = int(percentage_advance) # Int
        hours_worked_per_week = int(hours_worked_per_week) # Int

        # Getting divider to calculate
        divider = get_divider(hours_worked_per_week)

        # Calculating
        advance_payment_result = base_salary * (percentage_advance / 100)
        payment_by_hour_result = base_salary / divider
        payment_by_minute_result = (base_salary / divider) / 60
        
        # Formatting results
        formatted_advance_payment = format_currency(advance_payment_result, "BRL", locale="pt_BR")
        formatted_payment_by_hour = format_currency(payment_by_hour_result, "BRL", locale="pt_BR")
        formatted_payment_by_minute = format_currency(payment_by_minute_result, "BRL", locale="pt_BR")

        # Packaging values
        formatted_values = {
            "formatted_advance_payment": formatted_advance_payment,
            "formatted_payment_by_hour": formatted_payment_by_hour,
            "formatted_payment_by_minute": formatted_payment_by_minute,
        }

        return render_template("result.html", **formatted_values)