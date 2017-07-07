import requests
import random




class Hangman(object):

    def __init__(self):
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        hidden_word = random.choice(WORDS)
        print hidden_word
        self.game_main(hidden_word)


    def game_main(self, hidden_word):

        used_letters = ' '
        chances = 0
        good_guess = []

        while chances < 6:

            user_input = raw_input('Please enter a letter: ')

            if user_input in hidden_word and user_input not in used_letters:
                good_guess.append(user_input)
                used_letters += ' '.join(user_input)
                # print'Used Letters: %r' % used_letters
                # print 'Good Guess: %r' % good_guess
                # print hidden_word
                self.win_game(good_guess, hidden_word)


            elif user_input not in hidden_word and user_input not in used_letters:
                used_letters += ' '.join(user_input)
                chances += 1
                # print 'Chances: %r' % chances
                # print 'Used Letters: %r' % used_letters
                # print 'Good Guess: %r' % good_guess
                self.hangman_image(chances)

            elif user_input in used_letters:
                print 'Please enter another choice'


    def hangman_image(self, chances):
        if chances == 1:
            print """
                    |-----|
                    |      0
                    |
                    |
                    |________
                            """
        elif chances == 2:
            print """
                    |-----|
                    |      0
                    |      |
                    |
                    |________
                            """
        elif chances == 3:
            print"""
                    |-----|
                    |      0
                    |      |\
                    |
                    |________
                            """
        elif chances ==  4:
            print"""
                    |-----|
                    |      0
                    |     /|\
                    |
                    |________
                          """
        elif chances == 5:
            print"""
                    |-----|
                    |      0
                    |     /|\
                    |     /
                    |________
                          """
        elif chances == 6:
            print"""
                    |-----|
                    |      0
                    |     /|\
                    |     / \
                    |________
                          """



    def win_game(self, good_guess, hidden_word):
        winning_guesses = 0



















        # # for i, val in enumerate(hidden_word):
        # #     if hidden_word[i] == good_guess[i]:
        # while winning_guesses < 6:





game = Hangman()
