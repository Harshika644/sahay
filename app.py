from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Sahaay!"

@app.route('/lostfound')
def lostfound():
    return render_template('lostfound.html')  # Make sure lostfound.html exists in the templates folder

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

