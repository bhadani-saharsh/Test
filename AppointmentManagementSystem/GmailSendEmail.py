from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage
import base64
from datetime import datetime
from . import CredentialDetails

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
    plain_text += "\n\nAppointment request received on: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    plain_text += "\n\nRegards, \nAI Assistant,\nDr. Bhadani's Dental Clinic"
    return plain_text


def share_details_with_clinic(msgPlain):
    creds = CredentialDetails.create_credentials_gmail()
    try:
        service = build('gmail', 'v1', credentials=creds)
        msg = EmailMessage()
        msg.set_content(msgPlain)
        msg['Subject'] = "New Appointment Booked by AI"
        msg['From'] = "Donotreply@DrBhadanisDentalClinic.com"
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


def create_credentials():
    creds = Credentials(
        token="ya29.a0AXooCgslmG7ay9LBI6gy03bQTYesQs0FoIca1Mu5w4LC2YlspKvW08Mt50R3a2SN1KId-T1RmCcYl8LOaRQt6HfKglEpoxcvE5McQ5EvcEewPNJ6gSPRoCyjVlqSCAEw1NEdwLmpZFFeb_shKgasWjJEfnALTcrE6SZeUgaCgYKAd8SARMSFQHGX2MiiUOR1WN6dhym_HL8qiYPSg0173",
        refresh_token="1//0geeuYmwd-NDLCgYIARAAGBASNwF-L9IrS5Q5fRFtJKP9ANDdmO-_ZTIzJmTCXx6li4gu7DCPSl8Nk7KkPLS3LZtO-c5DbkpQ0o4",
        token_uri="https://oauth2.googleapis.com/token",
        client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com",
        client_secret="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",
        scopes=["https://mail.google.com/"],
        universe_domain="googleapis.com",
        account=""
        )
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
