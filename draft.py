solved = [1,2,3,4,5,6,7,8,'X'];
unsolved = [4,2,6,1,3,8,5,'X',7];
# [4,2,6]
# [1,3,8]
# [5,x,7]

# Helper Methods
def swap(array,index1,index2):
	temp = array[index1];
	array[index1]=array[index2];
	array[index2]=temp;
	# print str(temp)+' moved to position '+str(index2);
	# print str(array[index1])+' moved to position '+str(index1);
	return array;

def left(array):
	if(array.index('X')==0 or array.index('X')==3 or array.index('X')==6):
		print "Invalid move";
	else:
		swap(array,array.index('X'),array.index('X')-1);
		print "Slid left";
	return True;

def right(array):
	if(array.index('X')==2 or array.index('X')==5 or array.index('X')==8):
		print "Invalid move";
	else:
		swap(array,array.index('X'),array.index('X')+1);
		print "Slid right";
	return True;

def up(array):
	if (array.index('X')<3):
		print "Invalid move";
	else:
		swap(array,array.index('X'),array.index('X')-3);
		print "Slid up";
	return True;

def down(array):
	if (array.index('X')>5):
		print "Invalid move";
	else:
		swap(array,array.index('X'),array.index('X')+3);
		print "Slid down";
	return True;

def invalid(array):
	print "Invalid input";
	return False;

def slide(argument):
	# This function moves the empty space, X, in a given direction
    switcher = {
        'left': left,
        'right': right,
        'up': up,
        'down': down
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, invalid);
    # Execute the function
    return func(unsolved);

def printBoard(array):
	print '\n';
	print str(array[0])+' '+str(array[1])+' '+str(array[2]);
	# print '\r\n';
	print str(array[3])+' '+str(array[4])+' '+str(array[5]);
	# print '\r\n';
	print str(array[6])+' '+str(array[7])+' '+str(array[8]);
	print '\n';
	return True;

printBoard(unsolved);

game_in_progress = True;

while game_in_progress:
	move = raw_input('Enter a direction to move X: ');
	slide(move);
	printBoard(unsolved);
	if(unsolved == solved):
		print 'You win!!!';
		game_in_progress = False;
