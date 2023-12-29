import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('name_sheet')


def Introduction():
    """
    Message to appear when game is started.
    Instructions on how to play.
    """
    print("Welcome to the letter lair heh... heh... heh...")
    print("Where we play a little game called HANGMAN")
    print("Where you gotta find the hidden word or else...")
    print("You better win man or you gonna get hanged man... HaHaHaHA!")
    print()
    print("I'll give you a little info before we start:")
    print()
    print("1. Underscores signify each letter that makes up the hidden word.")
    print("2. Type a letter to start guessing the word.")
    print("3. Correct letters guessed, reveal all letter(s) in the word.")
    print("4. Each wrong guess and I will start to set up the HANGMAN he he")
    print("5. 6 incorrect guesses, you can guess what happens... (you lose).")
    print("6. Enjoy! he he he...")


Introduction()



