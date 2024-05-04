from google.oauth2.credentials import Credentials
import os.path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage
import base64
from datetime import datetime
import google.auth



SCOPES = ['https://mail.google.com/']


def create_plain_message(queryDict):
    plain_text = "Hi,\nAppointment request details are as follows:"
    plain_text += "\n\tEmail: " + queryDict['email']
    plain_text += "\n\tPatient's name: " + queryDict['fullname']
    plain_text += "\n\tMobile number: " + queryDict['phone']
    plain_text += "\n\tGender: " + queryDict['gender']
    plain_text += "\n\tAppointment date: " + queryDict['somedate']
    plain_text += "\n\tAppointment time: " + queryDict['appt']
    plain_text += "\n\tAddress: " + queryDict['address']
    plain_text += "\n\tChief complaints: " + queryDict['complaints']
    plain_text += "\n\nAppointment request received on: " + datetime.now().strftime("%d-%m-%y %H:%M:%S")
    plain_text += "\n\nRegards, \nAI Assistant,\nDr. Bhadani's Dental Clinic"
    return plain_text


def share_details_with_clinic(msgPlain):
    creds = create_credentials()
    try:
        service = build('gmail', 'v1', credentials=creds)
        msg = EmailMessage()
        msg.set_content(msgPlain)
        msg['Subject'] = "New Appointment Booked by AI"
        msg['From'] = "saharsh.bhadani.official@gmail.com"
        msg['To'] = "Saharsh.Bhadani@gmail.com"
        # msg['To'] = "Dr.HarshitBhadani@gmail.com"
        message = {'raw': base64.urlsafe_b64encode(msg.as_bytes()).decode()}
        try:
            send_message = (service.users().messages().send(userId="me",body=message).execute())
            print(f'Message Id: {send_message["id"]}')
            return "OK"
        except HttpError as error:
            print('An error occurred: %s' % error)
            return "Error"
    except HttpError as error:
        print(f"An error occurred: {error}")
        return "Error"


def create_credentials_short():
    creds, _ = google.auth.default()
    return creds


def create_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # Saharsh -- need to change this to run on server
    sub_folder = "/"#/AppointmentManagementSystem/"
    if os.path.exists(os.getcwd()+sub_folder+"gmail-token.json"):
        creds = Credentials.from_authorized_user_file(filename=os.getcwd()+sub_folder+"gmail-token.json", scopes=SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.getcwd()+sub_folder+"credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.getcwd()+sub_folder+"gmail-token.json", "w") as token:
            token.write(creds.to_json())
    return creds

if __name__ == "__main__":
    queryDict = {'csrfmiddlewaretoken': 'KOMHyZoJj663AyA0GndPNXhyWd2MVCm7Auh7kJUDqnwZ3GvQKlMBm9QWo3bvvkCO',
                  'email': 'saharsh.bhadani@gmail.com',
                 'fullname': 'Saharsh Bhadani',
                 'phone': '9168669610',
                 'gender': 'male',
                 'somedate': '2024-05-05',
                 'appt': '10:00',
                 'address': 'sdcajlsc acl',
                 'complaints': 'lc asckas caslc ',
                 'file_name': 'audio2024-05-0401-20-42-277Z.mp3'}
    plain_message = create_plain_message(queryDict)
    print(share_details_with_clinic(plain_message))
