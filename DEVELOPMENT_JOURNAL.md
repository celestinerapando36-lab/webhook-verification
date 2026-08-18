Webhook Verification Development Journal

Project Overview

Project: Webhook Verification Mini Prototype
Technology: Python and Flask
Authentication Method: HMAC-SHA256
Purpose: To build a Flask-based webhook endpoint that receives webhook requests and verifies their authenticity using an HMAC-SHA256 signature.

---

Development Journal

Date| Time| Activity| Error / Blocker| Resolution| Learning
18 Aug 2026| 1:00 PM| Started working on the webhook verification prototype and focused on understanding HMAC-SHA256 and how it would be used to authenticate webhook requests . Worked with the Python flask server and the "/webhook" endpoint.
.| Encountered issues while configuring and testing the webhook verification, i was initially unsure about the difference between Python, Flask and HTTP.| Reviewed the Flask application and corrected the configuration before continuing with testing.| Learned how a Flask server can provide an endpoint for receiving webhook requests and Python is the programming language, Flask is the web framework and HTTP is the communication protocol used for the webhook request.
18 Aug 2026| 2:10 PM| Generated a webhook secret for the verification process.| Initially had confusion about where the generated secret should be used.| Stored the secret securely and used it for generating and verifying HMAC signatures.| Learned that the secret is the private key used by HMAC to generate a signature.
18 Aug 2026| 3:00 PM| Studied HMAC-SHA256 and how it is used for webhook authentication.| Initially confused the secret with the generated signature.| Understood that the secret is used together with the message to produce the HMAC-SHA256 signature.| Learned that HMAC means Hash-based Message Authentication Code and SHA-256 is the hashing algorithm used.
18 Aug 2026| 3:15 PM| Tested the webhook endpoint without providing a signature.| The request was rejected because no signature was supplied.| Confirmed that the application returned "Missing signature".| Learned how negative testing can verify that required security information is being checked.
18 Aug 2026| 3:17 PM| Tested the webhook endpoint using an incorrect signature.| The signature did not match the expected HMAC signature.| Confirmed that the application returned "Invalid signature".| Learned how the application detects an unauthenticated or tampered request.
18 Aug 2026| 3:23 PM| Tested the webhook using a correctly generated signature.| Needed to confirm that the complete verification process worked.| Used the correct "X-Webhook-Signature" header and received HTTP "200 OK" with "Webhook verified successfully".| Learned how a valid HMAC signature allows the webhook request to be accepted.
18 Aug 2026| 10:45 PM| Moved the webhook secret into a ".env" file.| The secret needed to be separated from the source code.| Configured the application to obtain the secret through an environment variable.| Learned why sensitive credentials should not be hard-coded in application code.
18 Aug 2026| 10:50 PM| Installed the required Python environment-variable package.| The application required support for loading values from ".env".| Successfully installed the required package and continued testing.| Learned how Python packages can extend an application's functionality.
18 Aug 2026| 11:15 PM| Updated the webhook application to use the environment variable for the secret.| Needed to ensure the application still worked after changing how the secret was loaded.| Restarted Flask and repeated the webhook verification tests successfully.| Learned the importance of testing an application after changing its configuration.
18 Aug 2026| 11:45 PM| Began preparing the project for GitHub.| Git was initially not recognized as a command in PowerShell.| Added the Git installation directory to the current PowerShell PATH and confirmed the Git version.| Learned how PATH allows command-line programs to be located and executed.
18 Aug 2026| 11:47 PM| Initialized the local Git repository.| The repository initially had no commits.| Used "git init" to initialize the repository.| Learned that "git init" creates a Git repository for tracking project history.
18 Aug 2026| 11:56 PM| Checked the files detected by Git.| The ignore file had initially been named "gitignore.txt", causing ".env" to appear as an untracked file.| Renamed the file to ".gitignore" and confirmed that ".env" was no longer listed by Git.| Learned how ".gitignore" prevents sensitive or unwanted files from being tracked.
19 Aug 2026| 00:03 AM| Staged the project files for the first commit.| Initially entered the "git add" command incorrectly.| Corrected the command to "git add .".| Learned that "git add ." stages files in the current project while respecting ".gitignore".
19 Aug 2026| 00:10 AM| Created the first Git commit.| Git reported that the author identity was unknown.| Configured the Git user name and email address.| Learned that Git requires an author identity when creating commits.
19 Aug 2026| 00:14 AM| Created the first project commit.| No further blocker occurred.| Successfully created the commit using "git commit -m "Add webhook verification prototype"".| Learned that a commit creates a saved snapshot of staged project files.
19 Aug 2026| 00:16 AM| Connected the local repository to GitHub.| No major blocker occurred.| Added the GitHub repository as the "origin" remote and verified it using "git remote -v".| Learned how a local Git repository communicates with a remote GitHub repository.
19 Aug 2026| 00:18 AM| Authenticated Git with GitHub.| GitHub requested authorization for Git Credential Manager.| Authorized Git Credential Manager through the GitHub authentication page.| Learned how Git Credential Manager can handle GitHub authentication securely.
19 Aug 2026| 00:34 AM| Pushed the project to GitHub.| No blocker after authentication.| Successfully ran "git push -u origin master".| Learned how "git push" uploads local commits to the remote repository and establishes branch tracking.
19 Aug 2026| 00:37 AM| Verified the GitHub repository.| Needed to confirm that sensitive information had not been uploaded.| Confirmed that ".gitignore", "app.py", "generate_signature.py", and "webhook.py" were visible while ".env" was not.| Learned the importance of verifying that secrets remain excluded from public repositories.

Key Technical Concepts Learned

Flask

Flask is the Python web framework used to create the webhook server. The project uses a local endpoint similar to:

"http://127.0.0.1:5000/webhook"

The "/webhook" endpoint receives the incoming webhook request and performs signature verification.

HMAC-SHA256

HMAC stands for Hash-based Message Authentication Code.

HMAC-SHA256 uses a secret key and a message to produce a cryptographic signature. The receiving application can independently calculate the expected signature and compare it with the signature sent with the webhook request.

Environment Variables

The webhook secret was moved into a ".env" file instead of being stored directly in the Python source code. This reduces the risk of accidentally exposing sensitive credentials.

Git and GitHub

Git was used for version control, while GitHub was used to store the project remotely. The main Git commands learned during the project included:

- "git init" — initializes a Git repository.
- "git status" — shows the current state of the repository.
- "git add ." — stages files for a commit.
- "git commit" — saves a version of the project.
- "git remote -v" — displays the configured remote repository.
- "git push" — uploads commits to GitHub.

Final Reflection

This project helped me understand how webhook authentication works in a practical application. I learned how to create a Flask webhook endpoint and protect it using HMAC-SHA256 verification.

Testing the endpoint with no signature, an incorrect signature, and a valid signature helped me understand how authentication checks work in real applications. I also learned the difference between an HMAC secret and the signature generated from that secret.

Another important part of the project was learning how to protect sensitive information. Moving the webhook secret into a ".env" file and configuring ".gitignore" prevented the secret from being uploaded to GitHub.

The Git and GitHub process also gave me practical experience with version control. I learned how to initialize a repository, stage files, create commits, connect the local project to GitHub, authenticate using Git Credential Manager, and push the project to a remote repository.

Overall, the project improved my understanding of Python, Flask, webhook security, HMAC-SHA256, environment variables, debugging, Git, GitHub, and secure software development practices.
Overall, the project improved my understanding of Python, Flask, webhook security, HMAC-SHA256, environment variables, debugging, Git, GitHub, and secure software development practices.
