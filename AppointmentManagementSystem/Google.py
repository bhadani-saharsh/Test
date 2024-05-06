import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "15CuJsPYzfWeyCK2xhlG2zkKVZIQdAlL1Mb0JGBvwGKc"
SAMPLE_RANGE_NAME = "E:E"


def main():
    creds = create_credentials()
    # create_sheet(creds)
    result = read_sheet_data(creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)
    print(result)
    dates = result['values']
    closed_dates = ""
    if len(dates) > 1:
        today_date = datetime.now().date()
        closed_start_date = datetime.strptime(dates[1][0], '%d-%m-%Y').date()
        if closed_start_date > today_date:
            closed_dates ="?start="+closed_start_date.strftime('%Y-%m-%d')
        closed_end_date = datetime.strptime(dates[-1][0], '%d-%m-%Y').date()
        if closed_end_date > today_date:
            closed_dates += "&end=" + closed_end_date.strftime('%Y-%m-%d')
    return closed_dates
    # append_the_next_value(result, creds)

def prepare_changes_for_update(result):
    pass


def update_values(creds, spreadsheet_id, range_name, value_input_option, _val):
    try:
        service = build("sheets", "v4", credentials=creds)
        values = [
            [
                # Cell values ...
            ],
            # Additional rows ...
        ]
        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def append_the_next_value(result, creds):
    max = -1
    for row in result['values']:
        integer_value = -1
        try:
            integer_value = int(row[0])
        except ValueError:
            integer_value = -1

        if (integer_value != -1) & (integer_value > max):
            max = integer_value
    _val = str(int(max + 1))
    append_values(creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, "USER_ENTERED", _val)


def append_values(creds, spreadsheet_id, range_name, value_input_option, _val):
  """
  Creates the batch_update the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  # pylint: disable=maybe-no-member
  try:
    service = build("sheets", "v4", credentials=creds)
    values = [_val, _val, _val],

    body = {"values": values}
    result = (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body,
        )
        .execute()
    )
    print(f"{result.get('updatedCells')} cells updated.")
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error


def create_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # Saharsh -- need to change this to run on server
    sub_folder = "/AppointmentManagementSystem/"
    if os.path.exists(os.getcwd()+sub_folder+"sheets-token-json.py"):
        creds = Credentials.from_authorized_user_file(filename=os.getcwd()+sub_folder+"sheets-token-json.py", scopes=SCOPES)
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
        with open(os.getcwd()+sub_folder+"sheets-token-json.py", "w") as token:
            token.write(creds.to_json())
    return creds


def read_sheet_data(creds, spreadsheet_id, range_name):
    """
      Creates the batch_update the user has access to.
      Load pre-authorized user credentials from the environment.
      TODO(developer) - See https://developers.google.com/identity
      for guides on implementing OAuth2 for the application.
      """
    # pylint: disable=maybe-no-member
    try:
        service = build("sheets", "v4", credentials=creds)

        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=range_name)
            .execute()
        )
        rows = result.get("values", [])
        print(f"{len(rows)} rows retrieved")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def create_sheet(creds):
    try:
        title = "Datasheets"
        service = build("sheets", "v4", credentials=creds)
        spreadsheet = {"properties": {"title": title}}
        spreadsheet = (
            service.spreadsheets()
            .create(body=spreadsheet, fields="spreadsheetId")
            .execute()
        )
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get("spreadsheetId")
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == "__main__":
    main()
