from flask import Flask, render_template, request
from circle import calculate_area, calculate_circumference
from helper import perform_calculation, convert_to_float

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


@app.route('/calculateCircle', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def calculateCircle():
    resultArea = None
    resultPerimeter = None

    if request.method == 'POST':
        radius_str = request.form['value1']

        try:
            radius = float(radius_str)
        except ValueError:
            return render_template('Circle.html', resultArea="Invalid input for radius",
                                   resultPerimeter=resultPerimeter)

        operation = request.form.get('operation')

        if operation == 'area':
            resultArea = calculate_area(radius=radius)
        elif operation == 'perimeter':
            resultPerimeter = calculate_circumference(radius)
        else:
            return render_template('Circle.html', resultArea="Invalid operation", resultPerimeter=resultPerimeter)

        print(f"Radius: {radius}")
        print(f"Area: {resultArea}")
        print(f"Perimeter: {resultPerimeter}")
    return render_template('Circle.html', resultArea=resultArea, resultPerimeter=resultPerimeter)


if __name__ == '__main__':
    app.run(debug=True)
