from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

#POST and GET for /hello

@app.route("/hello", methods = ['GET'])
def hello():
   if request.method == 'GET':
	   return "Hello, world!"
   #if request.method == 'POST':
	#   return "The method has not been implemented", 405

#POST and GET for /check

@app.route("/check", methods = ['GET'])
def getmessage():
	   return "GET message received"
@app.route("/check", methods = ['POST'])
def postmessage():
    msg = request.args.get('msg',type=str)
    if not msg:
        abort(405)
    return"POST message received: "+msg;
	 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)