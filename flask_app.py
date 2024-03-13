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
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        if operation not in ['add', 'subtract', 'divide', 'multiply', 'circle_area', 'circle_perimeter']:
            return render_template('calculator.html',
                                   printed_result='Operation must be one of "add", "subtract", "divide", "multiply", "circle_area", or "circle_perimeter".')

        try:
            value1 = float(value1)
            value2 = float(value2)
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
    if request.method == 'POST':
        radius = request.form['radius']
        operation = request.form['operation']
        try:
            radius = float(radius)
            circle = Circle(radius)

            if radius <= 0:
                return render_template('circle.html', printed_result="Only positive radii are allowed.")
            elif operation == 'area':
                area = circle.area()
                printed_result = f"The area of a circle with radius {radius} is {area}"
                return render_template('circle.html', printed_result= printed_result)
            elif operation == 'perimeter':
                perimeter = circle.perimeter()
                printed_result = f"The perimeter of a circle with radius {radius} is {perimeter}"
                return render_template('circle.html', printed_result=printed_result)
        except ValueError:
            return render_template('circle.html', printed_result="Please enter a valid number for the radius")

    return render_template('circle.html')


if __name__ == "__main__":
    app.run(debug=True)
