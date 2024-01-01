from flask import Flask, request
import requests
import json
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == "__main__":
	app.run(port="7777",debug=True)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'


if __name__ == "__main__":
    print(f"My IP: {requests.get('https://api.my-ip.io/ip').text}")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT')))
