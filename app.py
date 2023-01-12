from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route("/text", methods=['GET', 'POST'])
def sms_reply():
    print("Recieved!")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
