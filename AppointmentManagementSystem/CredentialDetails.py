from google.oauth2.credentials import Credentials


SCOPES_DRIVE = ["https://www.googleapis.com/auth/drive.file"]
SCOPE_EMAIL = ['https://mail.google.com/']


def create_credentials_drive():
    return Credentials(token="ya29.a0AXooCgukiWNyYOwG1ku7Kp7N-3ry6bNhtfJiEYf4aHA0cpbstfx05oK5MHTBi8x_JTIrJ8OONLzPy1p9U_OgFDV7UEhw4aNN8eaHITNePmu_h93jaiQLK9vA77oj5OfAYWY5rm2V2Po82_psEZcTndh5QAwj4bucg688aCgYKAQUSARMSFQHGX2MiqIP7p380UN7Ccm76WF7XMA0171", refresh_token="1//0gxS6ILG6Iw-ICgYIARAAGBASNwF-L9IrqyyycgbLHTc1BdLyHX3Wdq1WRfo1Ira8cA3dNwwAu18quDjQorea6r-tsJArLdUgn7E", token_uri="https://oauth2.googleapis.com/token", client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com", client_secret="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", scopes="['https://www.googleapis.com/auth/drive.file']", universe_domain="googleapis.com", account="")

def create_credentials_gmail():
    return Credentials(token="ya29.a0AXooCgsUITHYW0Ou-JWNOU6IVbXjPOUKW7UAP4FDocZ1DeN7gTLorfxVgNwiw-majW6n83MlcR4PyXGDEDClviyVsswZKG-Z9yPJHUYABfC9pEG9b8xuFaqCAMuMvifJe96rgXk7rU7l9HwnztdqKxZTWmCwkBtrH48UaCgYKAbgSARMSFQHGX2MiepeDjCCwCyp2SRm8CKhr7w0171", refresh_token="1//0gUHn4yE8QKhzCgYIARAAGBASNwF-L9IrvwfJHj8s1_ssRwea7qhqZOuaAjQ2ziuuHH_ImRT-fd32Ik8eSzWCRsoPrD4lpzUai5A", token_uri="https://oauth2.googleapis.com/token", client_id="267226879829-n4pr2506kdmj0s9prb9mder7c291bf5c.apps.googleusercontent.com", client_secret="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", scopes="['https://mail.google.com/']", universe_domain="googleapis.com", account="")
    
