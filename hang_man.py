from collections import Counter
import get_random_word


class Hangman(object):

    secret_word = Counter(get_random_word.get_word())
    print secret_word

    def __init__(self):
        self.used_letters = ' '
        self.correct_guesses = 0
        self.bad_guesses = 0

    def get_user_guess(self):
        while True:
            self.user_guess = raw_input('Give a guess and hope for the best..: ')
            if len(self.user_guess) > 1 and not self.user_guess.al:
                print 'One letter at a time fool'
            else:
                break

    def check_user_guess(self):
        if self.user_guess in self.secret_word and self.user_guess not in self.used_letters:
            self.correct_guesses += self.secret_word[self.user_guess]
            self.used_letters += ' '.join(self.user_guess)
            self.play_game()
        elif self.user_guess not in self.secret_word:
            self.bad_guesses += 1
            self.used_letters += ' '.join(self.user_guess)
            self.hangman_image()
        elif self.user_guess in self.used_letters:
            print 'You tryna playin me sucka?'
            self.get_user_guess()
        #return self.correct_guesses - took this out and it added the values to correct_guesses, why?

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

    def play_game(self):
        while self.correct_guesses < sum(self.secret_word.values()):
                self.get_user_guess()
                self.check_user_guess()
        print 'You win muthasucka!'


game = Hangman()
game.play_game()
