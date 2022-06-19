from flask import Flask
feapp = Flask(__name__)

@feapp.route('/')
def hello_world():
    return 'myFrontEndService v1.0.1 (main) says Hello, Docker!'
