from google.oauth2.credentials import Credentials


SCOPES_DRIVE = ["https://www.googleapis.com/auth/drive.file"]
SCOPE_EMAIL = ['https://mail.google.com/']


def create_credentials_drive():
    return Credentials(token="ya29.a0AXooCgsmKKR5HW2NExDp7Fs9K04lIqOat3RGfpUrJ3aC_dlM3RNB3_653XqRXVSEaNSLbwngPbyK7fwCyRCiTDLOYCZpnZ2eGv4A6Ofnu3yssEOY0lw-lBy75Y1AEN-PGTxa8x96gFVVXKuUJ71OmPMm1373hZ_IXRq4aCgYKAdwSARMSFQHGX2Mij8OtjRK8ZBybqm4lvRnvYQ0171", refresh_token="1//0gFgieHccd_OkCgYIARAAGBASNwF-L9IrW4Oqp4jx0ZvS6zCXYuv3Wk-VlfcDaeR9p_H68oRRSzZpqujVvyj3CYSqmHqthTQHE0M", token_uri="https://oauth2.googleapis.com/token", client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com", client_secret="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", scopes="['https://www.googleapis.com/auth/drive.file']", universe_domain="googleapis.com", account="")

def create_credentials_gmail():
    return Credentials(token="ya29.a0AXooCgt_qqeTxrodkCo66xghLk3AbYTC63tLa6lB_aaP7vH3T10DufC-PxBSOAK6HkBjdnAE1g6xTq362o938fl_eWeYmF8js3-wSqrfky7gACgt5rhEiSBTHoRLFkxjqwNLYpygsW-RQ98P4qtCY5Dgnfd3Wgh9Gr3WaCgYKAQUSARMSFQHGX2Mi8Tk5fzSX23spgOeVOPi5pA0171", refresh_token="1//0gaW83SeNoZy_CgYIARAAGBASNwF-L9IrpJuq0kEbT1Py6dxbD9GhpiZgtKdJ0JxjWY-BbEwxDKBvRZ-YYSV43RerEgtEpp56HfM", token_uri="https://oauth2.googleapis.com/token", client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com", client_secret="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", scopes="['https://mail.google.com/']", universe_domain="googleapis.com", account="")
    
