#! usr/bin/env python

import random

def flip_coin():
    flip = random.choice(["heads", "tails"])
    return flip

# --------------------- Main program below ---------------------------------------



f = open("highScore.txt", "r+")

highScore = f.read()

highScore = int(highScore)

score = 0

name = raw_input("Hello, what is your name?")

print "Hello", name, "and welcome to the coin guessing game! The all-time high score is %d." % (highScore)

guess = raw_input("Heads or tails? ")

result = flip_coin()

while guess == result:
    score += 1
    print "It is %s. Great! Your score so far is %d. Keep going." % (result, score)
    guess = raw_input("Is it heads or tails?")
    result = flip_coin()

else:
    print "Nope. It's %s. Nice try. Your score is %d. The all-time high score is %d." % (result, score, highScore)




