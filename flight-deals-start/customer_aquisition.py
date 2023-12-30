import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1H3H_KzKXm1U-lTxpAsxd0KBv_G5qIYWyP3N-N6s5DOs'

def findFirstEmptyRow(service, sheet):

    done = False
    row = 1

    while not done:
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f'Sheet2!{row}:{row}').execute()
        values = result.get('values', [])

        if not values:
            return row
        else:
            row += 1
  
def buildSheetsService():
    
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
    
        service = build('sheets', 'v4', credentials=creds)
    
        return service
    
    except HttpError as error:
        return error

def fill_next_emtpy_row(service, sheet, row, values):

    body = {"values": values}

    return sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=f'Sheet2!A{row}:C{row}', valueInputOption='USER_ENTERED', body=body).execute()

def get_user_info():
    
        firstName = input("What is your first name? ")
        lastName = input("What is your last name? ")

        email = input("What is your email address? ")
        verify_email = input("Please verify your email address: ")

        while (email != verify_email):
            print("Emails do not match. Please try again.")
            email = input("What is your email address? ")
            verify_email = input("Please verify your email address: ")
    
        return [firstName, lastName, email]

def main():

    user_info = get_user_info()

    try:
        service = buildSheetsService()
        sheet = service.spreadsheets()
        firstEmptyRow = findFirstEmptyRow(service, sheet)
        newValues = [[user_info[0], user_info[1], user_info[2]]]

        result = fill_next_emtpy_row(service, sheet, firstEmptyRow, newValues)

        print(f"{result.get('updatedCells')} cells updated.")

    except HttpError as error:
        print(f'An error occured: {error}')
        return

    

if __name__ == '__main__':
  
  main()
