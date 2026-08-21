### Solo Recon

### What I Learned

For my Solo Recon, I chose to learn about **Webhook Verification using HMAC-SHA256**.

I learned:
- What webhooks are
- How HTTP requests work
- Why webhook verification is important
- How HMAC-SHA256 signatures are generated
- How a webhook request can be verified using a secret key
- How to reject requests with invalid signatures
  
### Webhook Verification Mini Prototype

### Project Overview

This project is a mini-prototype demonstrating how webhook requests can be authenticated using HMAC-SHA256.

The prototype was developed using Python and Flask. It receives a webhook request, checks the "X-Webhook-Signature" header, generates the expected HMAC-SHA256 signature using a secret key, and verifies whether the received signature is valid.

**Technologies Used**

- Python
- Flask
- HMAC-SHA256
- HTTP POST requests
- Git
- GitHub
- Python environment variables

### How the Prototype Works

The verification process follows these steps:

1. A webhook sends an HTTP "POST" request to the Flask "/webhook" endpoint.
2. The application checks for the "X-Webhook-Signature" header.
3. The application uses the webhook secret stored in an environment variable.
4. An expected HMAC-SHA256 signature is generated.
5. The received signature is compared with the expected signature.
6. The request is either accepted or rejected.

### Verification Flow

1.Receive Webhook: The Flask server receives an HTTP POST request at the /webhook endpoint.
             
2.Check signature: The application checks whether the X-Webhook-Signature header is present.
       
3.Retrieve secret:The webhook secret is loaded from the environment variable.
              
4.Generate Expected signature:The application generates an HMAC-SHA256 signature using the secret and request data.
       
5.Compare Signatures:The generated signature is compared with the signature received in the request.
       
6.Accept or reject:
  - If the signature matches the webhook is verified and returns HTTP 200 OK.
  - If the signature is missing or does not match, then the request is rejected.

### Project Files

[app.py](./app.py)

Runs the Flask application and provides the webhook endpoint.

[webhook.py](./webhook.py)

Contains the webhook verification logic.

[generate_signature.py](./generate_signature.py)

Generates an HMAC-SHA256 signature for testing the webhook.

[.gitignore](./.gitignore)

Prevents sensitive or unnecessary files from being committed to the repository.

**".env"**

Stores the webhook secret as an environment variable. This file is intentionally excluded from GitHub for security reasons.

### Testing

The prototype was tested using three main scenarios.

**Test 1 — Missing Signature**

A "POST" request was sent without the "X-Webhook-Signature" header.

Expected result:

Missing signature

The request was rejected.

**Test 2 — Invalid Signature**

A request was sent with an incorrect signature.

Expected result:

Invalid signature

The request was rejected.

**Test 3 — Valid Signature**

A request was sent using the correctly generated HMAC-SHA256 signature.

Result:

HTTP 200 OK

The webhook was successfully verified.

### Running the Prototype Locally

1. Install the required dependencies

Install Flask and the required environment-variable package in the Python environment.

2. Configure the environment variable

Create a ".env" file locally and add the webhook secret.

The ".env" file should not be uploaded to GitHub.

3. Start the Flask server

Run the Flask application from the terminal.

The server will run locally, for example:

http://127.0.0.1:5000

4. Test the webhook

Send a "POST" request to:

http://127.0.0.1:5000/webhook

Include the "X-Webhook-Signature" header when testing a valid request.

### Security Note

The webhook secret is stored locally in an environment variable rather than being hard-coded into the source code.

The ".env" file is excluded through ".gitignore" so that the secret is not exposed in the public repository.

### Learning Outcome

Through this prototype, I learned how webhook authentication works using HMAC-SHA256. I also gained practical experience with Flask, HTTP requests, environment variables, debugging, Git, GitHub, and GitHub authentication.

The prototype demonstrates the difference between a webhook secret and the generated authentication signature and shows how invalid or missing signatures can be rejected.
