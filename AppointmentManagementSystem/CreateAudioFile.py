# for text-to-speech
import io
import os
from tempfile import NamedTemporaryFile
from gtts import gTTS
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


SCOPES = ['https://www.googleapis.com/auth/drive.file']


def prepare_content_for_audio_file(query_dict):
    content_to_speak = "Please verify the provided details. The email address entered is "
    # Email address
    email_entered = query_dict['email']
    for index in range(len(email_entered)):
        if email_entered[index] == '.':
            content_to_speak += 'dot '
        elif email_entered[index] == '+':
            content_to_speak += 'plus '
        elif email_entered[index] == '-':
            content_to_speak += 'hyphen '
        elif email_entered[index] == '_':
            content_to_speak += 'Underscore '
        elif email_entered[index] == '~':
            content_to_speak += 'Tilde '
        elif email_entered[index] == '!':
            content_to_speak += 'Exclamation point '
        elif email_entered[index] == '#':
            content_to_speak += 'Hash '
        elif email_entered[index] == '$':
            content_to_speak += 'Dollar '
        elif email_entered[index] == '%':
            content_to_speak += 'Percent '
        elif email_entered[index] == '&':
            content_to_speak += 'and '
        elif email_entered[index] == '\'':
            content_to_speak += 'Single Quote '
        elif email_entered[index] == '\/':
            content_to_speak += 'Forward slash '
        elif email_entered[index] == '=':
            content_to_speak += 'Equal '
        elif email_entered[index] == '^':
            content_to_speak += 'Caret '
        elif email_entered[index] == '`':
            content_to_speak += 'Accent mark '
        elif email_entered[index] == '{':
            content_to_speak += 'Left curly brace '
        elif email_entered[index] == '}':
            content_to_speak += 'Right curly brace '
        elif email_entered[index] == '|':
            content_to_speak += 'Vertical bar'
        else:
            content_to_speak += email_entered[index] + " "
    # Name
    content_to_speak += ". The name entered is spelled as "
    full_name_entered = query_dict['fullname']
    for index in range(len(full_name_entered)):
        content_to_speak += full_name_entered[index] + " "
    # Mobile number
    content_to_speak += ". The mobile numbered entered is " + query_dict['phone'] + ". "
    # Gender
    content_to_speak += ". The gender entered is " + query_dict['gender'] + ". "
    # Appointment date
    appointment_date = query_dict['somedate']
    content_to_speak += ". The appointment is to be scheduled for " + str(int(appointment_date.split("-")[2])) + " "
    if appointment_date.split("-")[1] == '01':
        content_to_speak += 'January '
    elif appointment_date.split("-")[1] == '02':
        content_to_speak += 'February '
    elif appointment_date.split("-")[1] == '03':
        content_to_speak += 'March '
    elif appointment_date.split("-")[1] == '04':
        content_to_speak += 'April '
    elif appointment_date.split("-")[1] == '05':
        content_to_speak += 'May '
    elif appointment_date.split("-")[1] == '06':
        content_to_speak += 'June '
    elif appointment_date.split("-")[1] == '07':
        content_to_speak += 'July '
    elif appointment_date.split("-")[1] == '08':
        content_to_speak += 'August '
    elif appointment_date.split("-")[1] == '09':
        content_to_speak += 'September '
    elif appointment_date.split("-")[1] == '10':
        content_to_speak += 'October '
    elif appointment_date.split("-")[1] == '11':
        content_to_speak += 'November '
    elif appointment_date.split("-")[1] == '12':
        content_to_speak += 'December '
    content_to_speak += appointment_date.split("-")[0] + " at "
    # Appointment time
    appointment_time = query_dict['appt']
    content_to_speak += appointment_time.split(":")[0] + " "
    if appointment_time.split(":")[1] != "00":
        content_to_speak += appointment_time.split(":")[1]
    # Address and complaints
    content_to_speak += ". Also verify the address and complaint. " \
                        "If everything is alright then confirm otherwise " \
                        " make necessary corrections."
    return content_to_speak


def create_audio_file_and_upload_to_drive(text, file_name):
    speaker = gTTS(text=text, lang="en", slow=False)
    temp_file = NamedTemporaryFile(mode="wb", delete=False)
    speaker.write_to_fp(fp=temp_file)
    # speaker.save("mystaticfiles/"+file_name)
    file_id = upload_file_on_gdrive(temp_file, file_name)
    temp_file.close()
    os.unlink(temp_file.name)
    return file_id


def upload_file_on_gdrive(file_to_upload, file_name):
    import CredentialDetails
    creds = CredentialDetails.create_credentials_drive()
    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_metadata = {
            "name": file_name,
                         }
        media = MediaFileUpload(file_to_upload.name, mimetype="audio/mp3", resumable=True)
        # pylint: disable=maybe-no-member
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id, webViewLink")
            .execute()
        )
        print(f'File ID: {file.get("id")}')
        permission = {"type": "anyone", "role": "reader"}
        service.permissions().create(
            fileId=file.get("id"),
            body=permission,
        ).execute()
        return file.get("id")
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


def create_credentials():
    creds = Credentials(
        token="ya29.a0AXooCguL6CAP7xUOaxZZjmV5NLiVX2mGPnT8GfdEeY3I3XGGvVudToF9G8Yjez8-EIVYrHzASeloiReQEKXeBdYTg8wsTr7bAeYqbAIpl83Vf-PuD38YLXJDWCgLO8iNx4EWW9bS2sHNvokhlUMUD3LZGXoiNIdMVmIYaCgYKAbgSARMSFQHGX2MifS8cT0a2CQsQRFnNx3J9_Q0171",
        refresh_token="1//0g3S9m_pJYQ3aCgYIARAAGBASNwF-L9IrqQO5DjEyu3Kx8XEOIyvbeI2_9J-aayTqv8ljpEdKQLs8NsDlliahid1nY6hU2gl86yo",
        token_uri="https://oauth2.googleapis.com/token",
        client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com",
        client_secret="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",
        scopes=["https://www.googleapis.com/auth/drive.file"],
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
    content_to_speak = prepare_content_for_audio_file(queryDict)
    file_id = create_audio_file_and_upload_to_drive(content_to_speak, queryDict['file_name'])
    print(file_id)