import os
from flask import Flask, request
from send_sms import send_sms

app = Flask(__name__)

#TODO: create incoming messages route
username = 'YOUR_USERNAME_GOES_HERE'
api_key = 'YOUR_API_KEY_GOES_HERE'
africastalking.initialize(username, api_key)

#TODO: create delivery reports route.

if __name__ == "__main__":
    #TODO: Call send message function
    send_sms().sending()
    
    app.run(debug=True, port = os.environ.get("PORT"))