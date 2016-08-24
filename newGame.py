import random;
import csv;
import time;
import datetime;
import pandas as pd;
import copy as copy;

__DEBUG__ = True;
solved = [1,2,3,4,5,6,7,8,'X'];
puzzle = [1,2,3,4,6,'X',7,5,8];
current_state = copy.copy(puzzle);
player_moves = [];

def swap(array,index1,index2):
	temp = array[index1];
	array[index1]=array[index2];
	array[index2]=temp;
	return array;

def printBoard(array):
	print '\n';
	print str(array[0])+' '+str(array[1])+' '+str(array[2]);
	# print '\r\n';
	print str(array[3])+' '+str(array[4])+' '+str(array[5]);
	# print '\r\n';
	print str(array[6])+' '+str(array[7])+' '+str(array[8]);
	print '\n';
	return True;

def slide(array,direction):
	temp_array=copy.copy(array);
	if direction=="up":
		if (temp_array.index('X')<3):
			print "Invalid move";
			return False;
		else:
			output = swap(temp_array,temp_array.index('X'),temp_array.index('X')-3);
			print "Slid up";
			# player_moves.append('up');
		return output;
	elif direction=='down':
		if (temp_array.index('X')>5):
			print "Invalid move";
			return False;
		else:
			output = swap(temp_array,temp_array.index('X'),temp_array.index('X')+3);
			print "Slid down";
			# player_moves.append('up');
		return output;
	elif direction=='left':
		if(temp_array.index('X')==0 or temp_array.index('X')==3 or temp_array.index('X')==6):
			print "Invalid move";
			return False;
		else:
			output = swap(temp_array,temp_array.index('X'),temp_array.index('X')-1);
			print "Slid left";
			# player_moves.append('up');
		return output;
	elif direction=='right':
		if(temp_array.index('X')==2 or temp_array.index('X')==5 or temp_array.index('X')==8):
			print "Invalid move";
			return False;
		else:
			output = swap(temp_array,temp_array.index('X'),temp_array.index('X')+1);
			print "Slid right";
			# player_moves.append('up');
		return output;
	else:
		print "Move not understood";
		
def solver(temporary_array):
	# Should return the game board after performing chosen move
	# print possible_moves;
	possible_moves_for_this_turn = ["up","down","left","right"];
	# remove the opposite of the last move, since it negates previous turn
	if(len(player_moves)>0):
		last_move = player_moves[len(player_moves)-1]
		possible_moves_for_this_turn.remove(opposite(last_move));
	# Remove invalid moves
	if(temporary_array.index('X')==0 or temporary_array.index('X')==3 or temporary_array.index('X')==6):
		# cant move left
		possible_moves_for_this_turn.remove('left');
	if(temporary_array.index('X')==2 or temporary_array.index('X')==5 or temporary_array.index('X')==8):
		# cant move right
		possible_moves_for_this_turn.remove('right');
	if (temporary_array.index('X')<3):
		# cant move up
		possible_moves_for_this_turn.remove('up');
	if (temporary_array.index('X')>5):
		# cant move down
		possible_moves_for_this_turn.remove('down');
	# return random.choice(possible_moves_for_this_turn);
	scores = {};
	temp=copy.copy(temporary_array);
	print "TEMP = "+str(temp)

	for move in possible_moves_for_this_turn:
		print "Tried "+str(move)
		sum=0;
		# result is the game board after a potential move is performed
		result = slide(move,temp);
		print "result: "+str(result);
		# in case we dont have numpy
		for k in result:
			sum = sum+abs(result.index(k)-solved.index(k));
		scores[move] = sum;
		print move+" would cost "+str(sum);
	print min(scores.items());
	return slide(str(min(scores.items())));


game_in_progress=True;
while game_in_progress:
	printBoard(current_state);
	current_state=solver(current_state);