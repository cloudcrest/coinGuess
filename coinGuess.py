#! usr/bin/env python

import random

f = open("highScore.txt", "r+")

def flip_coin():
    flip = random.choice(["heads", "tails"])
    return flip


guess = raw_input("Heads or tails?")

result = flip_coin()

while guess == result:
    print "It is %s. Great! Keep going." % (result)
    guess = raw_input("Is it heads or tails?")
    result = flip_coin()

else:
    print "Nope. It's %s." % (result)




