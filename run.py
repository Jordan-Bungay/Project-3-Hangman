import gspread
from google.oauth2.service_account import Credentials
import random
import hangman_stages

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Define the constant variables
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('name_sheet')
CORRECT_GUESS_SCORE = 10
INCORRECT_GUESS_PENALTY = 5


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


def introduction():
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
    print("Underscores signify each letter that makes up the hidden word.")
    print("Type a letter to start guessing the word.")
    print("Correct letters guessed, reveal all letter(s) in the word.")
    print("Each wrong guess and I will start to set up the HANGMAN he he")
    print("6 incorrect guesses, you can guess what happens... (you lose).")
    print("Enjoy! he he he...")


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
            print(f"Hm? {user_data} didn't you.. Nevermind, welcome back!")
            return user_data
        else:
            print(f"{user_data} Good name to add to my colle.. welcome!\n")
            return user_data


def calculate_score(correct_guesses, incorrect_guesses):
    """
    Calculate the player's score.
    """
    return (
        correct_guesses * CORRECT_GUESS_SCORE
        - incorrect_guesses * INCORRECT_GUESS_PENALTY
    )


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


def get_chosen_letter(chosen_letters):
    """
    Gets the chosen letters.
    """
    return input("What's you guess?: \n").upper()


def update_display(chosen_word, chosen_letter, display):
    """
    Changes what is shown depending on the answer given by the user.
    """
    letter_chosen = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == chosen_letter:
            display[position] = chosen_word[position]
            letter_chosen = True
    return letter_chosen


def ready_to_play_status():
    """
    Ask the user if they want to play again
    """
    while True:
        decision = input("\nLet's go then?! [Y/N]? \n").upper()
        if decision == "Y":
            return True
        elif decision == "N":
            return False
        else:
            print("Hmm? I don't understand.. did you say 'Y' or 'N'?")


def execute_game():
    '''
    Handle the execution of the hangman game.
    '''
    introduction_executed = False
    saved_user = None

    while True:
        # Execute the introduction if it hasn't been shown yet
        if not introduction_executed:
            introduction()
            introduction_executed = True

        # Choices to start the game or not
        start_game = input(
            "\nAre you ready? heh heh (Y/N):\n"
        ).upper()

        if start_game != "Y":
            print("Aww leaving so soon... see you again soon he he, bye bye")
            break

        # Multiple rounds loop
        while True:
            ready_to_play = ready_to_play_status()

            if not ready_to_play:
                print("Aww leaving so soon.. see you again soon hehe, bye bye")
                return

            username = create_user(saved_user)
            score = play_game(username)
            update_score(username, score)
            saved_user = username

            play_again = input(
                "\nCome on you know you want to play again? hehehe (Y/N):\n"
            ).upper()

            if play_again != "Y":
                print("Aww leaving so soon.. see you again soon hehe, bye bye")
                return


def play_game(username):
    """
    Play out the game.
    Putting together most of the functons to play the game out
    """
    chosen_word = random_word()  # Choose a random word
    display = hidden_word_underline(chosen_word)  # Underline the hidden word

    # Variables
    lives = 6
    chosen_letters = []
    correct_guesses = 0
    incorrect_guesses = 0
    game_over = False

    print("He he he what is the word?: " + " ".join(display))
    while not game_over:
        print("Ooh interesting!, you chose: " + ' '.join(chosen_letters))
        # Play a turn and get the updated state
        lives, chosen_letters, display, letter_chosen = play_turn(
            chosen_word, lives, chosen_letters, display
        )

        # Calculate score
        score = calculate_score(correct_guesses, incorrect_guesses)

        if letter_chosen:
            correct_guesses += 1
        else:
            incorrect_guesses += 1

        print("He he he what is the word?: " + " ".join(display))

        # Check if the hidden word has been guessed correctly
        if "_" not in display:
            game_over = True
            score = calculate_score(correct_guesses, incorrect_guesses)
            print(f"\nDamn! I mean well done! The word was: {chosen_word}")
            print(f"Your score: {score}")
        elif lives == 0:
            game_over = True
            print("\nHa Ha time to get Hang, Man The word was: " + chosen_word)

    return score


def play_turn(chosen_word, lives, chosen_letters, display):
    """
    Plays a single turn of the game.
    """
    print("\nBe careful he he, you have:", lives)

    # Letter chosen by the player
    chosen_letter = get_chosen_letter(chosen_letters)

    if not check_valid_letter(chosen_letter):
        print("Hmm? I don't understand what letter from A-Z did you say?")
        return lives, chosen_letters, display, False

    if chosen_letter in chosen_letters:
        print("Are you trying to trick me? You have already said that letter.")
        return lives, chosen_letters, display, False

    # Update chosen letter in chosen letters
    chosen_letters.append(chosen_letter)
    letter_chosen = update_display(chosen_word, chosen_letter, display)

    # If the chosen_letter is incorrect, show the hangman stage
    if not letter_chosen:
        lives -= 1
        print("\nWrong! That's one step closer to Hangman he he.")
        print("Hangman stage:")
        print(hangman_stages.stages[lives])
    else:
        print("\nooh that would be a correct answer...")

    return lives, chosen_letters, display, letter_chosen


execute_game()
