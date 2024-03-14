# Import Flask class
from flask import Flask, render_template, request
from helper import perform_calculation, convert_to_float
from helper_circle import circle_perform

# Create Flask object
app = Flask(__name__)  # create the instance of the flask class

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#Creating home route and returning home HTML
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

#Creating circle route and returning circle HTML
@app.route('/circle', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def circle():
    printed_result = None

    if request.method == 'POST':
        radius = float(request.form['radius'])
        operation = request.form['operation']

        # Create an instance
        helper_circle = circle_perform(radius)

        if radius < 0:
            printed_result = 'Radius must not be defined as negative.'
        elif operation not in ['Perimeter', 'Area']:
            printed_result = 'Operation must be one of "Perimeter", or "Area".'
        elif operation == 'Perimeter':
            result = helper_circle.perimeter()
            printed_result = f"Perimeter: {result}"
        else:
            result = helper_circle.area()
            printed_result = f"Area: {result}"

    return render_template('circle.html', printed_result=printed_result)