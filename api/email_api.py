import os
from google.auth import exceptions
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load the credentials from the 'credentials.json' file
try:
    creds = service_account.Credentials.from_service_account_file(
        os.path.join(os.getcwd(), 'credentials.json'),
        scopes=['https://www.googleapis.com/auth/gmail.modify']
    )
except exceptions.DefaultCredentialsError as e:
    print(f"Failed to load credentials: {e}")
    exit(1)

# Build the Gmail API service
try:
    service = build('gmail', 'v1', credentials=creds)
except HttpError as e:
    print(f"Failed to connect to the Gmail API: {e}")
    exit(1)

def get_email_chain(user_id, email_id):
    """Retrieve the email chain for the given user_id and email_id."""
    try:
        email_chain = service.users().messages().get(userId=user_id, id=email_id).execute()
        return email_chain
    except HttpError as e:
        print(f"Failed to get email chain: {e}")
        return None

def send_reply(user_id, email_id, reply):
    """Send a reply to the given user_id and email_id with the specified reply message."""
    try:
        message = service.users().messages().send(userId=user_id, body=reply).execute()
        print(f"Message Id: {message['id']}")
        return message
    except HttpError as e:
        print(f"Failed to send reply: {e}")
        return None