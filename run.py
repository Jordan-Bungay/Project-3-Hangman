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


def get_sheet_data():
    """
    Get data from the names sheet.
    Each entry in the data includes the username, score, and index.
    """
    try:
        names_sheet = SHEET.get_worksheet(0)
        records = names_sheet.get_all_records()
        data = [
            {
                'username': entry['username'],
                'score': entry['score'],
                'index': i + 2
            }
            for i, entry in enumerate(records)
        ]
        return data
    except Exception as e:
        print(f"Error retrieving sheet data: {e}")
        return []


get_sheet_data()


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


def create_user(existing_user=None):
    """
    Create new user.
    Get existing user from sheet.
    """
    while True:
        if existing_user:
            print(f"Hmm? {existing_user}, Didn't you, nevermind welcome back!")
            return existing_user

        data_user = input("Ahh where are my manners... What is your name?\n")

        # Check if the user is already saved in the sheet
        user_saved = any(
            entry['names'] == data_user for entry in get_sheet_data()
        )

        if user_saved:
            print(f"Hmm? {data_user}, Didn't you, nevermind welcome back!")
            return data_user
        else:
            print(f"hehe thats a good one! {data_user} Let's play!\n")
            return data_user


create_user(existing_user=None)



