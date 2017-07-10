from collections import Counter
import getword_mod


class Hangman(object):

    secret_word = Counter(getword_mod.get_word())
    print secret_word
    def __init__(self):
        self.used_letters = ' '
        self.correct_guesses = 0


    def check_user_guess(self):
        if  user_guess in secret_word and user_guess not in used_letters:
            self.correct_guesses += self.secret_word[self.user_guess]
        elif self.user_guess not in self.secret_word:
            self.used_letters += ' '.join(self.user_guess)
            print 'This is the: %r' % self.correct_guesses

#     def play_game(self, user_guess):
#         user_guess = raw_input('Enter a letter: ')
#         while self.correct_guesses < sum(Hangman.values(secret_word)):
#             user_guess = raw_input('Please enter a guess: ')
            

game = Hangman()
game.check_user_guess()
game.play_game(game)
