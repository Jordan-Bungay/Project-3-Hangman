import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('name_sheet')
CORRECT_GUESS_SCORE = 10
INCORRECT_GUESS_PENALTY = 5


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


def create_user(saved_user=None):
    """
    Ask the user for their name.
    Get saved user if already played.
    """
    while True:
        if saved_user:
            print(f"Hm? {saved_user} didn't you.. Nevermind, welcome back!")
            return saved_user

        user_data = input("Ahh where are me manners! What's your name?\n")

        # Check if the username already exists in the sheet
        saved_username = any(
            entry['username'] == user_data for entry in get_sheet_data()
        )

        if saved_username:
            print(f"Hm? {saved_user} didn't you.. Nevermind, welcome back!")
            return user_data
        else:
            print(f"{data_username} Good name to add to my colle.. welcome!\n")
            return user_data


def get_sheet_data():
    """
    Get data from the name_sheet.
    Each entry in the data includes the username, score, and index.
    """
    try:
        name_sheet = SHEET.get_worksheet(0)
        records = name_sheet.get_all_records()
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
        print(f"Getting data from sheet error: {e}")
        return []


def update_score(username, score):
    """
    Update the name_sheet with new username and score.
    If the username already exists, add the new score to the old score.
    """
    try:
        name_sheet = SHEET.get_worksheet(0)
        data = get_sheet_data()

        # Is there already a saved user
        saved_username = any(entry['username'] == username for entry in data)

        if saved_username:
            # Updates the saved players score with the new score
            for entry in data:
                if entry['username'] == username:
                    entry['score'] += score
                    name_sheet.update_cell(entry['index'], 2, entry['score'])
                    print(f"Updated score for {username} to {entry['score']}")
                    break
        else:
            # If there is not a saved user, add a new user
            new_user = [username, score]
            name_sheet.append_row(new_user)
            print(f"Added a new row for {username} with the score {score}")

            # Update the local data with the new data
            data = get_sheet_data()

        print("Your score has been updated")
    except Exception as e:
        print(f"Score update error: {e}")


def random_word():
    """
    Get a word from the words.txt and set it to uppercase.
    """
    try:
        with open("words.txt", "r") as file:
            rand_words = file.readlines()
        return random.choice(rand_words).strip().upper()
    except FileNotFoundError:
        print("words.txt could not be found. Make sure the file exists.")
        exit()


def hidden_word_underline(word):
    """
    Creates the underline for the hidden word.
    """
    return ["_" for _ in word]


def check_valid_letter(chosen_letter):
    """
    Checks if the letter that has been input is valid.
    """
    return chosen_letter.isalpha() and len(chosen_letter) == 1


def calculate_score(correct_guesses, incorrect_guesses):
    """
    Calculate the player's score.
    """
    return (
        correct_guesses * CORRECT_GUESS_SCORE  # Constant variable
        - incorrect_guesses * INCORRECT_GUESS_PENALTY  # Constant variable
    )
