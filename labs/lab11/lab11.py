"""
Name: Michael Diorio
lab11.py
"""
from random import randint


def read_words(word_list):
    infile = open(word_list, "r")
    words = []
    for line in infile:
        words.append(line.strip())
    return words


def pick_secret_word(words):
    secret_word = words[randint(1, len(words))]
    return secret_word


def guessed_word(secret_word, letter, guess_word, guessed_letters):
    check = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            # fix
            check = True
    if check:
        return True


def guess_letter(guessed_letters, guess_word, secret_word):
    letter = input("Guess a letter: ")
    check = False
    while not check:
        for i in guessed_letters:
            if letter == i:
                print("Letter has been previously guessed, try another.")
                letter = input("Guess a letter: ")
                letter = letter.lower()
        if (ord(letter) > 122 or ord(letter) < 97) and len(letter) != 1:
            print("Not a valid character, try again.")
            letter = input("Guess a letter: ")
            letter = letter.lower()
        if guessed_word(secret_word, letter, guess_word, guessed_letters):
            return True
        else:
            return False


def secret_word_spelled(guess_word, secret_word):
    return bool(" ".join(guess_word) == secret_word)


def game_specifics(guess_word, guessed_letters, turn_count):
    print("Guessed word: ", guess_word)
    print("Guessed letters: ", guessed_letters)
    print("Guesses remaining: ", turn_count)


def play_game():
    turn_count = 7
    secret_word = pick_secret_word(read_words("wordlist.txt"))
    guessed_letters = " "
    guess_word = "_ " * len(secret_word)
    print(game_specifics(guess_word, guessed_letters, turn_count))
    while turn_count != 0:
        if not guess_letter(guessed_letters, guess_word, secret_word):
            turn_count = turn_count - 1
            print(game_specifics(guess_word, guessed_letters, turn_count))
    if turn_count == 0:
        print("You did not guess the word, game over!")
    else:
        print("You guessed the word, you win!")


def main():
    play_game()
    pass


main()
