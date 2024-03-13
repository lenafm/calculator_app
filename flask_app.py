# Data Structures & Algorithms Spring 2024
# Problem Set 2
# Lonny Chen, 216697
# flask_app.py

from flask import Flask, render_template, request
from helper import perform_calculation, convert_to_float
from circle import Circle

app = Flask(__name__)  # create the instance of the flask class

# route() decorator tells Flask: base URL triggers index "home page"
@app.route('/')
@app.route('/home')
def home():
    '''Home page template'''
    return render_template('home.html')

# route() decorator tells Flask: '/calculate' URL triggers calculation
@app.route('/calculate', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def calculate():
    '''Calculation of mathematical operation from HTML form values, includes input error checking.'''

    if request.method == 'POST':
        # using the request method from flask to request the values that were sent to the server through the POST method
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])
        rounding = request.form['rounding']

        # make sure the input is one of the allowed inputs (not absolutely necessary in the drop-down case)
        if operation not in ['add', 'subtract', 'divide', 'multiply']:
            return render_template('calculator.html',
                                   printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

        try:
            value1 = convert_to_float(value=value1)
            value2 = convert_to_float(value=value2)
            rounding_int = int(float(rounding))
            assert rounding_int >= 0
        except ValueError:
            return render_template('calculator.html', printed_result="Entered values should be numbers!")
        except AssertionError:
            return render_template('calculator.html', printed_result="Rounding should not be negative!")

        try:
            result = perform_calculation(value1=value1, value2=value2, operation=operation, rounding_int=rounding_int)
            printed_result = f'The result of {value1} {operation} {value2} is: {result} (rounded to {rounding_int} decimals)'
            return render_template('calculator.html', printed_result=printed_result)

        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="You cannot divide by zero")

    return render_template('calculator.html')

# route() decorator tells Flask: '/circle' URL triggers circle calculation
@app.route('/circle', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def circle():
    '''Calculation of circle calculation from HTML form values, includes input error checking.'''

    if request.method == 'POST':
        # using the request method from flask to request the values that were sent to the server through the POST method
        radius = request.form['radius']
        operation = str(request.form['operation'])
        rounding = request.form['rounding']

        # make sure the input is one of the allowed inputs (not absolutely necessary in the drop-down case)
        if operation not in ['perimeter', 'area']:
            return render_template('circle.html',
                                   printed_result='Operation must be one of "perimeter" or "area".')

        try:
            radius = convert_to_float(value=radius)
            rounding = convert_to_float(value=rounding)
            assert radius >= 0 and rounding >= 0
        except ValueError:
            return render_template('circle.html', printed_result="Entered values should be numbers!")
        except AssertionError:
            return render_template('circle.html', printed_result="Radius or rounding should not be negative!")

        # Circle class calculations
        rounding_int = int(rounding)
        circle = Circle(float(radius))
        if operation == 'perimeter':
            result = circle.perimeter(rounding_int)
        else:
            result = circle.area(rounding_int)
        printed_result = f'For a circle with radius of {radius}, the {operation} is: {result} (rounded to {rounding_int} decimals)'

        return render_template('circle.html', printed_result=printed_result)

    return render_template('circle.html')

# So web app can be refreshed in browser after changes
# Can just enter on command line: "python flask_app.py"
if __name__ == '__main__':
    app.run(debug=True)