import random
from words import words
from hangman_visual_representation import lives_visual_dict
import string


# To remove Whitespace and dash
def get_valid_word(words):
    word = random.choice(words)  # choose a word from the list randomly
    while '-' in words or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # user guessed
    lives = 7

    # User input
    while len(word_letters) > 0 and lives >0:
        # Show letter used
        print('You have', lives, 'lives left')
        print('You have used these letters', ' '.join(used_letters))

        # What is the current word is(updated W _ R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print('\n Your letter,', user_letter, 'is not in the word')

        elif user_letter in used_letters:
            print('You have used this letter.Please try again')
        else:
            print('Invalid character. Please try again')
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
if __name__ == '__main__':
    hangman()

