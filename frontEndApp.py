from flask import Flask
feapp = Flask(__name__)

@feapp.route('/')
def hello_world():
    return 'myFrontEndService v1.0.1 (mnfb-1.1) says Hello, Docker!'
