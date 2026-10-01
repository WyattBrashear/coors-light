from flask import Flask, request
import flask_cors
import requests

app = Flask(__name__)
# Must run at import time: Vercel/gunicorn import the module and never execute __main__,
# so CORS headers would otherwise be missing in production.
flask_cors.CORS(app)

@app.route('/get')
def index():
    url = request.args.get('url')
    if not url:
        return 'Missing "url" query parameter', 400
    response = requests.get(url)
    return response.text, response.status_code

@app.route('/post', methods=['POST'])
def post():
    url = request.args.get('url')
    if not url:
        return 'Missing "url" query parameter', 400
    response = requests.post(url, data=request.json)
    return response.text, response.status_code

if __name__ == '__main__':
    app.run()
