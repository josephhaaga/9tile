# BoardGenerator.py
# ------------------------------
# This script generates a shuffled board with a solvable configuration.

# I'm skeptical that every random permutation of the solved board results in a solvable configuration,
# so this will guarantee input boards are solvable.

import HelperFunctions;
import random;
from game import *;

# numberOfMoves = 100;

# numOfMoves denotes how many transforms the output will undergo.
def generate(numOfMoves):
	solved = [1,2,3,4,5,6,7,8,'X'];
	unsolved = solved;
	possible_moves = ['up','down','left','right'];
	while(solved==unsolved):
		for x in range(0,numOfMoves):
			random_move = random.choice(possible_moves);
			unsolved = HelperFunctions.slide(random_move);
	return unsolved;
