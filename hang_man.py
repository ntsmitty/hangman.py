from collections import Counter
import getword_mod


class Hangman(object):

    secret_word = Counter(getword_mod.get_word())
    #print secret_word

    def __init__(self):
        self.used_letters = ' '
        self.correct_guesses = 0
        self.bad_guesses = 0

    def get_used_guess(self):
        self.user_guess = raw_input('Please enter letter: ')
        #print self.correct_guesses
        #print self.secret_word[self.user_guess]
        return self.user_guess

    def validate_user_guess(self):
        print 'we here dawg'
        if self.user_guess in self.secret_word and self.user_guess not in self.used_letters:
            self.correct_guesses += self.secret_word[self.user_guess]
            self.used_letters += ' '.join(self.user_guess)
        elif self.user_guess not in self.secret_word:
            self.bad_guesses += 1
            self.used_letters += ' '.join(self.user_guess)
        #return self.correct_guesses - took this out and wokred, why?

    def win_game(self):
        print 'We good'
        while self.correct_guesses < sum(self.secret_word.values()):
            if self.bad_guesses == 6:
                print 'You Lose'
                break
            else:
                #print self.correct_guesses
                self.get_used_guess()
                self.validate_user_guess()


game = Hangman()
game.win_game()
