import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel","rangers","tree","house","beekeeper","beautiful"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

string=(chosen_word)
list1=list(string)


lives=6

print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You loose")
            
    print(f"Lives left: {lives}")
    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You won.")

    print(stages[lives])
