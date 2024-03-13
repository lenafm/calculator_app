from flask import Flask, render_template, request

from helper import perform_calculation, convert_to_float

from circle import Circle

from test_circle import test_circle_area, test_circle_perimeter

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
def circle():
    area = None # default
    perimeter = None # default
    radius = None  # default
    printed_result = ""
    if request.method == 'POST':
        radius_str = request.form.get('radius')
        if radius_str:
            try:
                radius = float(radius_str)
                if radius > 0:
                    circle_obj = Circle(radius)
                    area = "{:.2f}".format(circle_obj.area())
                    perimeter = "{:.2f}".format(circle_obj.perimeter())
                else:
                    # If radius is not greater than 0, reset it to None and set the error message
                    radius = None
                    printed_result = "Radius must be a positive number."
            except ValueError:
                # If there's a ValueError, reset radius to None and set the error message
                radius = None
                printed_result = "Please enter a valid number for the radius."
    return render_template('circle.html', radius=radius, area=area, perimeter=perimeter, printed_result=printed_result)

# Optional: Run app in debug Mode including the tests
# if __name__ == '__main__':
#     test_circle_area()
#     test_circle_perimeter()
#     app.run(debug=True)