import hashlib
import time
import sys
arguments = sys.argv;
total = []
#print str(arguments);
def hash(start):
	start = start;
	stop = start + 1000000;
	current = start;
	list = []


	while(current<=stop):
		hashme = str(current)
		hashed = hashlib.sha512(hashme).hexdigest()
		list.append(hashed)
		current = current +1
		
		
	

timestart = time.time()
arguments.pop(0);
for argument in arguments:
	#print argument;
	hash(int(argument))
	finalnumlist = hashlib.sha512(str(list)).hexdigest();
	total.append(finalnumlist);
#print total;
finalhash = str(total);
print hashlib.sha512(finalhash).hexdigest()
timeend =  time.time()
#print timeend-timestart
