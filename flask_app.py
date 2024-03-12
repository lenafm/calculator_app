from flask import Flask, render_template, request

from helper import perform_calculation, convert_to_float
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

@app.route('/circle', methods=['GET', 'POST'])
def calculate_circle():
    radius = ''  # Set a default value for radius as empty string
    if request.method == 'POST':
        # using the request method from flask to request the values that were sent to the server through the POST method
        radius = request.form.get('radius')

    try:
        radius = convert_to_float(value=radius)
    except ValueError:
        return render_template('circle.html', printed_result_area="Please type digits")


    if radius is not None:
        create_circle = Circle(float(radius))  # Convert radius to float
        calc_area = create_circle.circle_area()
        calc_per = create_circle.circle_perimeter()
        return render_template('circle.html', printed_result_area=str(calc_area), printed_result_per=str(calc_per))
    else:
        return render_template('circle.html', printed_result="Radius not provided")
