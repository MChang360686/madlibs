# This project is an easy exercise in using f strings
# and the random package

import random

# take inputs from user
verb1 = input("verb: ")
adjective1 = input("adjective: ")
adverb2 = input("adverb: ")
noun2 = input("noun: ")
pronoun3 = input("pronoun: ")
verb3 = input("verb: ")

# concatenation using f strings

plotlineOne = f"No time to explain, {verb1} a {adjective1} cactus!  The BBEG is a {adverb2} {noun2} \
that will {verb3} {pronoun3} if we don't hurry up"

plotLineTwo = f"who keeps {adverb2} stealing my apples?  I bet it's {noun2}, isn't it \
you scoundrel?  I will {adverb2} write a letter to the {noun2} and {pronoun3} will {verb3} you \
from this plane of existence"

plotlineThree = f"{pronoun3} had to {verb3} the cow lest it consume us all.  Because of this, the " \
                f"{adverb2} {adjective1} {noun2} ended it rightly, and the cow {verb1}"

# driver code
if __name__ == "__main__":
    print(random.choice([plotlineOne, plotLineTwo, plotlineThree]))
