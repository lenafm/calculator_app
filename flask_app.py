from flask import Flask, render_template, request
from helper import perform_calculation, convert_to_float
## We need this package in order to perform the circle calculations
from circle import Circle

app = Flask(__name__)  # create the instance of the flask class


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/calculate', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def calculate():
    if request.method == 'POST':
        # using the request method from flask to request the values that were sent to the server through the POST method
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        # make sure the input is one of the allowed inputs (not absolutely necessary in the drop-down case)
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


### Aranxa Márquez: PS_2

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    printed_result = None  # Initialize printed_result variable

    if request.method == 'POST':
        radius = float(request.form['radius'])  # Correctly extract radius from form data
        operation = request.form['operation']

        circle = Circle(radius)  # Create a Circle instance with the given radius

        if operation == 'perimeter':
            result = circle.perimeter_calculation()
            printed_result = f"The perimeter of the circle is: {result}"
        elif operation == 'area':
            result = circle.area_calculation()
            printed_result = f"The area of the circle is: {result}"
        else:
            printed_result = 'Operation must be one of "area", "perimeter"'

    return render_template('circle.html', printed_result=printed_result)