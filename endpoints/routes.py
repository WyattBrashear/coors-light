from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/get/<url>')
def index(url):
    response = requests.get(url)
    return response.text

@app.route('/post/<url>', methods=['POST'])
def post(url):
    response = requests.post(url, data=request.json)
    return response.text

if __name__ == '__main__':
    app.run()
