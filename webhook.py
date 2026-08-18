#Gives python the ability to load the values from .env into your program
from dotenv import load_dotenv
import os

load_dotenv()

# Import Flask tools for creating our web server and handling requests
from flask import Flask, request, jsonify

# Import security tools for creating and comparing webhook signatures
import hmac
import hashlib

# Create the Flask application 
app = Flask(__name__) 

# Secret key shared between the webhook sender and our application
#Python, go to the environment variables and get the value stored under the name
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

# Create a webhook endpoint that accepts POST requests
@app.route("/webhook",
methods=["POST"])
def verify_webhook():
	# Get the signature sent by the webhook sender
	signature = request.headers.get("X-Webhook-Signature")
	# Reject the request if no signature was provided
	if not signature:
		return jsonify({"error":"Missing signature"}), 401
	# Get the actual data sent in the webhook request
	payload= request.get_data()

	# Calculate the signature that we expect
        # This uses our secret key and the webhook data
	expected_signature = hmac.new(
		WEBHOOK_SECRET.encode(),
		payload,
		hashlib.sha256
	).hexdigest()

	 # Compare the received signature with our expected signature	
	if not hmac.compare_digest(signature,expected_signature):

		# Reject the webhook if the signatures do not match
		return jsonify({"error":"Invalid signature"}), 401
	return jsonify({"message":"Webhook verified successfully"}), 200
if __name__ == "__main__":
	app.run()
