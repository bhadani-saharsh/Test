# for text-to-speech
import datetime
import os
import time

from gtts import gTTS


def prepare_content_for_audio_file(QueryDict):
    content_to_speak = "Please verify the provided details. The email address entered is "
    # Email address
    email_entered = QueryDict['email']
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
    full_name_entered = QueryDict['fullname']
    for index in range(len(full_name_entered)):
        content_to_speak += full_name_entered[index] + " "
    # Mobile number
    content_to_speak += ". The mobile numbered entered is "+QueryDict['phone']+". "
    # Gender
    content_to_speak += ". The gender entered is " + QueryDict['gender'] + ". "
    # Appointment date
    appointment_date = QueryDict['somedate']
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
    appointment_time = QueryDict['appt']
    content_to_speak += appointment_time.split(":")[0] + " "
    if appointment_time.split(":")[1] != "00":
        content_to_speak += appointment_time.split(":")[1]
    # Address and ccomplaints
    content_to_speak += ". Also verify the address and complaint. " \
                        "If everything is alright then confirm otherwise " \
                        " make necessary corrections."
    return content_to_speak

def create_audio_file(text, file_name):
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("mystaticfiles/"+file_name)
    statbuf = os.stat("mystaticfiles/"+file_name)
    mbytes = statbuf.st_size / 1024
    duration = mbytes / 200
    time.sleep(int(50 * duration))
