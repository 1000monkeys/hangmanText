# This is a sample Python script.
from random import randint


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Letter:
    guessed = False
    in_word = False
    letter = ""

    def __init__(self, letter, in_word):
        self.letter = letter
        self.in_word = in_word

    def get_letter(self):
        return self.letter

    def get_in_word(self):
        return self.in_word

    def toggle_guessed(self):
        self.guessed = True

    def get_guessed(self):
        return self.guessed


def get_word():
    words = [
        "chthonic",
        "squush",
        "kickshaw",
        "zugzwang",
        "ytterbium",
        "randkluft",
        "yclept",
        "diphthong",
        "squdgy"
    ]

    return words[randint(0, len(words) - 1)]


def get_word_string(word):
    word_string = ""
    for letter in word:
        if letters[alphabet_string.find(letter)].get_guessed() is True:
            word_string += letter
        else:
            word_string += "_"

    return word_string


def amount_wrong():
    wrong_count = 0
    for i in range(len(letters)):
        if letters[i].get_guessed() is True and letters[i].get_in_word() is False:
            wrong_count += 1

    return wrong_count


def get_tried_letters_string():
    letters_string = ""
    for i in range(len(letters)):
        if letters[i].get_guessed():
            letters_string += letters[i].get_letter()

    return letters_string


def set_clean_letters(word):
    for i in range(len(alphabet_string)):
        letters[i] = Letter(alphabet_string[i], alphabet_string[i] in word)


def finished():
    all_guessed = True
    for i in range(len(alphabet_string)):
        if letters[i].get_guessed() is False and letters[i].get_in_word() is True:
            all_guessed = False
            break

    return all_guessed


def try_again():
    try_again_input = input("Try again? yes/no")

    if try_again_input == "yes":
        global word
        word = get_word()
        if debug:
            print(word)

        set_clean_letters(word)
    else:
        print("Goodbye!")
        exit()


debug = False
running = True
alphabet_string = "abcdefghijklmnopqrstuvwxyz"
letters = [None] * 26
word = get_word()

if __name__ == '__main__':
    if debug:
        print(word)

    set_clean_letters(word)

    if debug:
        for letter in letters:
            print(letter.get_letter())
            print(letter.get_in_word())
            print(letter.get_guessed())
            print("\n\n")

    while running:
        print("Which letter do you want to guess?")
        print("You have tried these letters:")
        print(get_tried_letters_string())
        print("This is the word:")
        print(get_word_string(word))
        letter = input("Please guess a letter:")
        letter = letter[0]

        if letter in get_tried_letters_string():
            print("You already guessed this letter!")
            continue
        else:
            letter_alphabet_position = alphabet_string.find(letter)

            if debug:
                print(letter_alphabet_position)

            letters[letter_alphabet_position].toggle_guessed()

            if letters[letter_alphabet_position].get_in_word():
                print("You guessed correctly!")
            else:
                print("This letter is not in the word!")
                print("You have " + str(amount_wrong()) + " wrong, You have 3 chances!")

        print("\n\n")

        if finished() is True:
            print(get_word_string(word))
            print("You guessed the entire word!")
            try_again()

        if amount_wrong() > 2:
            print("You lost!")
            try_again()
