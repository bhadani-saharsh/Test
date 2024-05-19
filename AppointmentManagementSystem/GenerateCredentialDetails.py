from google.oauth2.credentials import Credentials
import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES_DRIVE = ["https://www.googleapis.com/auth/drive.file"]
SCOPE_EMAIL = ['https://mail.google.com/']

TOP_LINES = '''from google.oauth2.credentials import Credentials


SCOPES_DRIVE = ["https://www.googleapis.com/auth/drive.file"]
SCOPE_EMAIL = ['https://mail.google.com/']


def create_credentials_drive():
    return Credentials({0})

def create_credentials_gmail():
    return Credentials({1})
    
'''


def create_credentials_drive():
    creds = Credentials(
        token="ya29.a0AXooCguL6CAP7xUOaxZZjmV5NLiVX2mGPnT8GfdEeY3I3XGGvVudToF9G8Yjez8-EIVYrHzASeloiReQEKXeBdYTg8wsTr7bAeYqbAIpl83Vf-PuD38YLXJDWCgLO8iNx4EWW9bS2sHNvokhlUMUD3LZGXoiNIdMVmIYaCgYKAbgSARMSFQHGX2MifS8cT0a2CQsQRFnNx3J9_Q0171",
        refresh_token="1//0g3S9m_pJYQ3aCgYIARAAGBASNwF-L9IrqQO5DjEyu3Kx8XEOIyvbeI2_9J-aayTqv8ljpEdKQLs8NsDlliahid1nY6hU2gl86yo",
        token_uri="https://oauth2.googleapis.com/token",
        client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com",
        client_secret="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",
        scopes=SCOPES_DRIVE,
        universe_domain="googleapis.com",
        account=""
    )
    return creds


def create_credentials_email():
    creds = Credentials(
        token="ya29.a0AXooCguL6CAP7xUOaxZZjmV5NLiVX2mGPnT8GfdEeY3I3XGGvVudToF9G8Yjez8-EIVYrHzASeloiReQEKXeBdYTg8wsTr7bAeYqbAIpl83Vf-PuD38YLXJDWCgLO8iNx4EWW9bS2sHNvokhlUMUD3LZGXoiNIdMVmIYaCgYKAbgSARMSFQHGX2MifS8cT0a2CQsQRFnNx3J9_Q0171",
        refresh_token="1//0g3S9m_pJYQ3aCgYIARAAGBASNwF-L9IrqQO5DjEyu3Kx8XEOIyvbeI2_9J-aayTqv8ljpEdKQLs8NsDlliahid1nY6hU2gl86yo",
        token_uri="https://oauth2.googleapis.com/token",
        client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com",
        client_secret="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",
        scopes=SCOPE_EMAIL,
        universe_domain="googleapis.com",
        account=""
    )
    return creds


def generate_credentials_drive():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # Saharsh -- need to change this to run on server
    sub_folder = "/"
    if os.path.exists(os.getcwd() + sub_folder + "gdrive-token-json.py"):
        creds = Credentials.from_authorized_user_file(filename=os.getcwd() + sub_folder + "gdrive-token-json.py",
                                                      scopes=SCOPES_DRIVE)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.getcwd() + sub_folder + "credentials.json", SCOPES_DRIVE
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.getcwd() + sub_folder + "gdrive-token-json.py", "w") as token:
            token.write(creds.to_json())
    return creds


def write_drive_credentials_to_file():
    sub_folder = "/"
    details_of_drive_file = None
    details_of_gmail_file = None
    if os.path.exists(os.getcwd() + sub_folder + "gdrive-token-json.py"):
        with open(os.getcwd() + sub_folder + "gdrive-token-json.py", 'r') as file:
            details_of_drive_file = file.read().rstrip()
    if os.path.exists(os.getcwd() + sub_folder + "gmail-token-json.py"):
        with open(os.getcwd() + sub_folder + "gmail-token-json.py", 'r') as file:
            details_of_gmail_file = file.read().rstrip()
    content_to_write = prepare_content_to_write(details_of_drive_file, details_of_gmail_file)
    if os.path.exists(os.getcwd() + sub_folder + "CredentialDetails.py"):
        with open(os.getcwd() + sub_folder + "CredentialDetails.py", 'r+') as file:
            file.write(content_to_write)
            file.close()


def prepare_content_to_write(details_of_drive_file, details_of_gmail_file):
    Dict_drive = eval(details_of_drive_file)
    inner_content_1 = "token=\""
    inner_content_1 += Dict_drive["token"]
    inner_content_1 += "\", refresh_token=\""
    inner_content_1 += Dict_drive["refresh_token"]
    inner_content_1 += "\", token_uri=\""
    inner_content_1 += Dict_drive["token_uri"]
    inner_content_1 += "\", client_id=\""
    inner_content_1 += Dict_drive["client_id"]
    inner_content_1 += "\", client_secret=\""
    inner_content_1 += Dict_drive["client_secret"]
    inner_content_1 += "\", scopes=\""
    inner_content_1 += str(Dict_drive["scopes"])
    inner_content_1 += "\", universe_domain=\""
    inner_content_1 += Dict_drive["universe_domain"]
    inner_content_1 += "\", account=\""
    inner_content_1 += Dict_drive["account"]
    inner_content_1 += "\""

    Dict_gmail = eval(details_of_gmail_file)
    inner_content_2 = "token=\""
    inner_content_2 += Dict_gmail["token"]
    inner_content_2 += "\", refresh_token=\""
    inner_content_2 += Dict_gmail["refresh_token"]
    inner_content_2 += "\", token_uri=\""
    inner_content_2 += Dict_gmail["token_uri"]
    inner_content_2 += "\", client_id=\""
    inner_content_2 += Dict_gmail["client_id"]
    inner_content_2 += "\", client_secret=\""
    inner_content_2 += Dict_gmail["client_secret"]
    inner_content_2 += "\", scopes=\""
    inner_content_2 += str(Dict_gmail["scopes"])
    inner_content_2 += "\", universe_domain=\""
    inner_content_2 += Dict_gmail["universe_domain"]
    inner_content_2 += "\", account=\""
    inner_content_2 += Dict_gmail["account"]
    inner_content_2 += "\""
    content_to_write = TOP_LINES.format(inner_content_1, inner_content_2)
    return content_to_write

def generate_credentials_email():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # Saharsh -- need to change this to run on server
    sub_folder = "/"
    if os.path.exists(os.getcwd() + sub_folder + "gmail-token-json.py"):
        creds = Credentials.from_authorized_user_file(filename=os.getcwd() + sub_folder + "gmail-token-json.py",
                                                      scopes=SCOPE_EMAIL)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.getcwd() + sub_folder + "credentials.json", SCOPE_EMAIL
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.getcwd() + sub_folder + "gmail-token-json.py", "w") as token:
            token.write(creds.to_json())
    return creds

def delete_existing_files():
    sub_folder = "/"
    if os.path.exists(os.getcwd() + sub_folder + "gmail-token-json.py"):
        os.remove(os.getcwd() + sub_folder + "gmail-token-json.py")
    else:
        print("gmail-token-json.py does not exist.")
    if os.path.exists(os.getcwd() + sub_folder + "gdrive-token-json.py"):
        os.remove(os.getcwd() + sub_folder + "gdrive-token-json.py")
    else:
        print("gdrive-token-json.py does not exist.")


if __name__ == "__main__":
    delete_existing_files()
    generate_credentials_email()
    generate_credentials_drive()
    write_drive_credentials_to_file()

