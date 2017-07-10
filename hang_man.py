from collections import Counter
import getword_mod


class Hangman(object):

    secret_word = Counter(getword_mod.get_word())
    print secret_word
    
    #correct_guesses should not exceed the length of the secret_word, when it is equal - you win.
    def __init__(self):
        self.used_letters = ' '
        self.correct_guesses = 0
        self.user_guess = raw_input('Enter a letter: ')

    def validate_user_guess(self):
        if self.user_guess in self.secret_word and self.user_guess not in self.used_letters:
            self.correct_guesses += self.secret_word[self.user_guess]
            self.used_letters += ' '.join(self.user_guess)
        elif self.user_guess not in self.secret_word:
            self.used_letters += ' '.join(self.user_guess)
        return self.correct_guesses



game = Hangman()
game.validate_user_guess())
