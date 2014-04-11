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

print "Hello", name, "and welcome to the coin guessing game! The all-time high score is %d, held by NAME HERE." % (highScore)

guess = raw_input("Heads or tails?")

result = flip_coin()

while guess == result:
    print "It is %s. Great! Keep going." % (result)
    guess = raw_input("Is it heads or tails?")
    result = flip_coin()
    score += 1

else:
    print "Nope. It's %s. Nice try. Your high score is %d. The all-time high score is %d." % (result, score, highScore)




