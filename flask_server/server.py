
import logging
import json, os

from flask import request, Response, render_template, jsonify, Flask
from pywebpush import webpush, WebPushException

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"private_key.txt")
DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(),"public_key.txt")

VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")
dummydb = {"subscription" : None }
VAPID_CLAIMS = {
"sub": "mailto:develop@raturi.in"
}
def saveToDatabase(subscription):
    dummydb["subscription"]=subscription
def send_web_push(subscription_information, message_body):
    # print(subscription_information["subscription_token"])
    return webpush(
        subscription_info=subscription_information["subscription_token"],
        data=message_body,
        vapid_private_key=VAPID_PRIVATE_KEY,
        vapid_claims=VAPID_CLAIMS
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/save-subscription", methods=["POST"])
def subscription():
    """
        POST creates a subscription
        GET returns vapid public key which clients uses to send around push notification
    """
    subscription_token = request.get_json("subscription_token")
    saveToDatabase(subscription_token)
    return Response(status=201, mimetype="application/json")

@app.route("/push/",methods=['get'])
def push():
    subscription = dummydb["subscription"]
    message = "Hi"
    send_web_push(subscription,message)
    return jsonify({'success':1})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)