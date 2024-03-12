# flask_app.py

from flask import Flask, render_template, request
from circle import Circle  # Import Circle from the circle module
from helper import perform_calculation, convert_to_float

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        if operation not in ['add', 'subtract', 'divide', 'multiply']:
            return render_template('calculator.html',
                                   printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

        try:
            value1 = convert_to_float(value=value1)
            value2 = convert_to_float(value=value2)
        except ValueError:
            return render_template('calculator.html', printed_result="Cannot perform operation with this input")

        try:
            result = perform_calculation(value1=value1, value2=value2, operation=operation)
            return render_template('calculator.html', printed_result=str(result))

        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="You cannot divide by zero")

    return render_template('calculator.html')


@app.route('/calculate_perimeter_area', methods=['GET', 'POST'])
def calculate_perimeter_area():
    perimeter_result = None
    area_result = None

    if request.method == 'POST':
        radius = request.form['radius']

        try:
            radius = convert_to_float(radius)
        except ValueError:
            return render_template('perimeter_calculator.html', printed_result="Please enter a valid number for the radius.")

        if radius <= 0:
            return render_template('perimeter_calculator.html', printed_result="Radius must be a positive number.")

        circle = Circle(radius)
        perimeter_result = circle.calculate_perimeter()
        area_result = circle.calculate_area()

        print("Perimeter Result:", perimeter_result)
        print("Area Result:", area_result)

    return render_template('perimeter_calculator.html', perimeter_result=perimeter_result, area_result=area_result)

if __name__ == '__main__':
    app.run(debug=True)
