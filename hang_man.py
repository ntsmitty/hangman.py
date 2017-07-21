from collections import Counter
import get_random_word
import string


class Hangman(object):

    secret_word = Counter(get_random_word.get_word())
    #print secret_word

    def __init__(self):
        self.used_letters = ' '
        self.correct_guesses = 0
        self.bad_guesses = 0

    def get_user_guess(self):
        print self.used_letters
        while True:
            self.user_guess = raw_input('Give a guess and hope for the best..: ')
            if len(self.user_guess) <= 1 and self.user_guess.isalpha():
                return self.user_guess
            else:
                print 'Try again sucka ass!'
                self.get_user_guess()

    def check_user_guess(self):
        if self.user_guess in self.secret_word and self.user_guess not in self.used_letters:
            self.correct_guesses += self.secret_word[self.user_guess]
            self.used_letters += ' '.join(self.user_guess)
            self.win_game()
        elif self.user_guess not in self.secret_word:
            self.bad_guesses += 1
            self.used_letters += ' '.join(self.user_guess)
            self.hangman_image()
        elif self.user_guess in self.used_letters:
            print 'You tryna playin me sucka?'
            self.get_user_guess()

    def hangman_image(self):
        if self.bad_guesses == 1:
            print    "   |-----|     "
            print    "   |      0    "
            print    "   |           "
            print    "   |           "
            print    "   |           "
            print    "   |_________  "

        elif self.bad_guesses == 2:
            print    "   |-----|     "
            print    "   |      0    "
            print    "   |      |    "
            print    "   |           "
            print    "   |           "
            print    "   |_________  "

        elif self.bad_guesses == 3:
            print    "   |-----|     "
            print    "   |      0    "
            print    "   |     /|    "
            print    "   |           "
            print    "   |           "
            print    "   |_________  "
        elif self.bad_guesses ==  4:
            print    "   |-----|     "
            print    "   |      0    "
            print    "   |     /|\   "
            print    "   |           "
            print    "   |           "
            print    "   |_________  "
        elif self.bad_guesses == 5:
            print    "   |-----|     "
            print    "   |      0    "
            print    "   |     /|\   "
            print    "   |     /     "
            print    "   |           "
            print    "   |_________  "

        elif self.bad_guesses == 6:
            print    "   |-----|     "
            print    "   |      0    "
            print    "   |     /|\   "
            print    "   |     / \   "
            print    "   |           "
            print    "   |_________  "
            print 'you dead fool'
            exit()

    def win_game(self):
        while self.correct_guesses < sum(self.secret_word.values()):
                self.get_user_guess()
                self.check_user_guess()
        print 'You win muthasucka!'

game = Hangman()
game.win_game()
