from flask import Flask, request

app = Flask(__name__)

# Homepage route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Greet User route
@app.route('/greet', methods=['GET', 'POST'])
def greet_user():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f'Hello, {name}! You are {age} years old.'
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
