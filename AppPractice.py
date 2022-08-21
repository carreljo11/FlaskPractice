from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return"""
        <html>
            <body>
                <h1> This is the main page </h1>
            </body>
        </html>
    """

@app.route('/wiki')
def get_data():
    return request.get('https://wikipedia.org').content



