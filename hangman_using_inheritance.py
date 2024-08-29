import random

print('''
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
''')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

class HangmanGame:
    def __init__(self):
        self.lives = 6
        self.selected_word = random.choice(words)
        self.encrypted_word = ["_"] * len(self.selected_word)
        self.guess_word = list(self.selected_word)

    def match_word(self, user_input):
        is_matched = False
        for index, letter in enumerate(self.guess_word):
            if letter == user_input:
                self.encrypted_word[index] = letter
                is_matched = True
        return is_matched

    def call_guess(self):
        user_input = input("Guess a letter (a-z): ").lower()
        print("\n")
        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter only one valid letter at a time.")
            return None
        return user_input

    def control_game_state(self, is_guess_true):
        if not is_guess_true:
            self.lives -= 1
            print(f"Wrong guess! {self.lives} chances left.")
            print(' '.join(self.encrypted_word))
            print(HANGMANPICS[6 - self.lives])
            if self.lives == 0:
                print("Game over! The word was: " + self.selected_word)
                return True
        else:
            print(' '.join(self.encrypted_word))
            print("Good job! Try your next guess.")
            if "_" not in self.encrypted_word:
                print("You Win!")
                print(f"The word was: {self.selected_word}")
                return True
        return False

    def start_game(self):
        print(' '.join(self.encrypted_word))
        while True:
            user_input = self.call_guess()
            if user_input:
                state = self.match_word(user_input)
                if self.control_game_state(state):
                    break


class AdvancedHangmanGame(HangmanGame):
    def __init__(self):
        super().__init__()
       
if __name__ == "__main__":
    game = HangmanGame() 
    game.start_game()
