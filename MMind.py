#Filename: MMind.py
#Description: text based MasterMind game

import random
COLORS = 6 #default to 6 colors numbered 0,1,2,...,5
SPACES = 4 #default to 4 spaces

#returns a tuple [#black, #white] for the number of correct colors in the correct locations, 
#number of correct colors in the incorrect locations, respectively
def scoreGuess(secret, guess):
  numBlack = sum([secret[i]==guess[i] for i in range(SPACES)])
  s_counts = [sum([secret[i]==j for i in range(SPACES)]) for j in range(COLORS)]
  g_counts = [sum([guess[i]==j for i in range(SPACES)]) for j in range(COLORS)]
  numWhite = sum([min(s_counts[i],g_counts[i]) for i in range(COLORS)])-numBlack
  return [numBlack,numWhite]

#generates a random secret sequence
def genSecret():
  l = []
  for i in range(SPACES):
    l.append(random.randint(0,COLORS-1))
  return l

#parses a guess
def parseString(g):
  guess = []
  for i in g:
    guess.append(int(i))
  return guess

if __name__ == "__main__":
  import sys
  if len(sys.argv)==3:
    COLORS = int(sys.argv[1])
    SPACES = int(sys.argv[2])
  gameOver = False
  Round = 1
  secret = genSecret()
  print "MasterMind!"
  print "Make a guess of length",SPACES,"entered as a string using 'colors' from 0,1,2,...,",COLORS-1
  while (not gameOver) and (Round < 9):
    print "****** Round ",Round," ******"
    g = list(raw_input("What is your guess? "))
    while len(g)!= SPACES:
      print "The length must be",SPACES
      g = list(raw_input("What is your guess? "))
    guess = parseString(g)
    pegs = scoreGuess(secret,guess)
    print "Number black = ",pegs[0],"Number white = ",pegs[1]
    if pegs[0]==SPACES: gameOver=True
    Round +=1
  if gameOver: print "You Win!"
  else:
    print "You Lose!"
    print "The answer was",secret

