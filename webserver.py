from flask import Flask, request, render_template_string
import time  # Add delay

app = Flask(__name__)

# HTML template for the calculator
calculator_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="POST">
        <input type="number" name="num1" placeholder="First Number" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="num2" placeholder="Second Number" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    time.sleep(0.5)  # Add delay to slow down the server
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."

    return render_template_string(calculator_html, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)  # Disable threading for inefficiency
