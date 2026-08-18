#Gives python the ability to load the values from .env into your program
from dotenv import load_dotenv
import os

load_dotenv()

import hmac
import hashlib

# The same secret used by our webhook application
secret = os.getenv("WEBHOOK_SECRET").encode()

# The exact webhook message we are testing
payload = b'{"message":"Test webhook"}'

# Generate the correct HMAC-SHA256 signature
signature = hmac.new(
    secret,
    payload,
    hashlib.sha256
).hexdigest()

# Display the signature
print(signature)