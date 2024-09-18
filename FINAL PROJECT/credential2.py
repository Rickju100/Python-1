import gspread
from google.oauth2.service_account import Credentials

# Define the OAuth scopes you need
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Load credentials from the JSON file you downloaded
credentials_filename = "D:/Programación/Software Development/Python 1/FINAL PROJECT/credentials.json"

# Create credentials object with scopes
credentials = Credentials.from_service_account_file(credentials_filename, scopes=SCOPES)

# Authenticate with Google Sheets API
client = gspread.authorize(credentials)

# Open the spreadsheet using the key
spreadsheet = client.open_by_key("1nv6NsjrdKNmBROi1IfDJMgajhfsg4cLbTSyRljH8niQ")

# Access the first sheet
sheet = spreadsheet.sheet1
