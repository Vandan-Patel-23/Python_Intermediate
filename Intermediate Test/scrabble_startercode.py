'''
SCRABBLE TEST STARTER CODE
Coder: [Vandan]
Date: [Monday 18,2024]

It's always good practice to leave a comment at the top of a big project.
This way if you want to look back at this project in a few years, you can see when you wrote it
and what it does.

Write a brief description of this project here.

'''

'''
If your project needs any modules (it does), your import statements should go here
'''
import random as r
# Here are some data structures you will need for the project. They are GLOBAL variables
with open("C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Intermidiate\\Collins Scrabble Words (2019).txt") as f:
    valid_words = set(line.strip().upper() for line in f)

# TILES contains all the same tiles as a scrabble bag, with the same quantities too
TILES = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A',
         'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'R', 'T', 'N',
         'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'L', 'S', 'U', 'L', 'S', 'U', 'L',
         'S', 'U', 'L', 'S', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'C', 'M', 'P', 'B', 'C', 'M', 'P',
         'F', 'H', 'V', 'W', 'Y', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']

# tile_to_points maps a letter to the number of points it is worth when played
tile_to_points = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                  'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
                  'Q': 10, 'Z': 10}

'''
You should have been given a file 'Collins Scrabble Words (2019).txt'.
This file contains all valid scrabble words, in all uppercase, with one per line.
Open the file, read the contents into a list.
Your list 'valid_words' should contain every word from the file, each word being its own element.
Remember a line in a file always ends with a newline character, account for this somehow.
When you are done reading the file, make sure it is closed.
'''

## FUNCTION SPACE ##

# GAME PLAY FUNCTIONS #
# by creating these two input sanitization functions, our later code is much cleaner


def int_input(prompt):
    int_user = input(prompt)
    while not int_user.isdigit():
        int_user = input(prompt)
    return int(int_user)
#test for int_input
# a=int_input('Enter 1/0:')
# print(a,type(a))

def str_input(prompt):
    str_user = input(prompt)
    while not str_user.isalpha():
        str_user = input(prompt)
    return str_user.upper()

# test for str_input
# b=str_input('Enter something:')
# print(b,type(b))

def get_new_tiles(num):
    new_hand = r.sample(TILES, num)
    for i in new_hand:
        TILES.remove(i)
    return new_hand

# test for get_new_tiles
# c= get_new_tiles(9)
# print(c,type(c))

def print_hand(hand):
    for i in hand:
        print(i,' : ',tile_to_points[i])

#Test for print hand
# print_hand(c)

def get_points(word):
    points = 0
    for i in word:
        points+=tile_to_points[i]
    return points
# test for get_points
# print(get_points('HELLO'))

def is_valid_play(word, hand):
    if len(word) > 7 or len(word) < 1:
        return False
    word = word.upper()
    if word not in valid_words:
        return False
    for char in word:
        if char not in hand:
            return False
        if word.count(char) > hand.count(char):
            return False
    return True
# GAME STATISTIC FUNCTIONS #


def get_winner():
    max_points = max(player_to_points.values())
    winners = [player for player, points in player_to_points.items() if points == max_points]
    return winners


def get_best_word(player_words):
    best_word = ""
    best_score = 0
    for word in player_words:
        score = get_points(word)
        if score > best_score:
            best_score = score
            best_word = word
    return best_word


## GAME STARTS ##


'''
There is nothing to be added or changed in this section! Skip down to 
line 190 for your next tasks.
'''

num_players = int_input("Number of players: ")
player_to_words = {}  # maps a player to the words they have played
player_to_points = {}  # maps a player to the points they have earned
player_to_hand = {}  # maps a player to a list of the tiles in their hand

# initialising all the dictionaries
for i in range(1, num_players + 1):
    name = str_input("Enter name of player {}: ".format(i))
    player_to_words[name] = []
    player_to_points[name] = 0
    player_to_hand[name] = get_new_tiles(7)

'''MAIN GAME LOOP 
this section contains the part of the game that repeats until the game is over
the game is over if they run out of tiles or players choose to stop
'''

choice= None
while len(TILES) > 0 and choice != 1:
    print("---- NEW ROUND ----")
    for player in player_to_words:
        print("-- {}'s TURN --".format(player))
        print_hand(player_to_hand[player])
        print("Options for your turn:")
        print("0 - pick new tiles")
        print("1 - play word")
        print("Any other number - STOP GAME")
        choice = int_input("Enter a number to select: ")

        if choice == 0:
            TILES.extend(player_to_hand[player])
            player_to_hand[player] = get_new_tiles(7)
            print_hand(player_to_hand[player])
            print("END OF TURN")

        elif choice == 1:
            word = str_input("Enter the word to play: ")
            if not is_valid_play(word, player_to_hand[player]):
                print("INVALID GUESS - TURN SKIPPED")
            else:
                player_to_words[player].append(word)
                points = get_points(word)
                print("Your word earned", points, "points!")
                player_to_points[player] += points
                for char in word:
                    player_to_hand[player].remove(char)
                player_to_hand[player].extend(get_new_tiles(len(word)))
                print("UPDATED HAND:")
                print_hand(player_to_hand[player])

        else:
            print("STOPPING GAME...")
            break

print("GAME OVER - GENERATING GAME STATS")
winners = get_winner()
if len(winners) == 1:
    print("CONGRATULATIONS TO THE WINNER:", winners[0])
else:
    print("IT'S A TIE! The winners are:", ", ".join(winners))
for player, words in player_to_words.items():
    print("{}'s highest scoring word: {}".format(player, get_best_word(words)))
