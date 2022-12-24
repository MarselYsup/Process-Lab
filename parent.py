#!/usr/bin/python3

import os
import sys
import random

def exec_child(time):
	os.execv("child.py",["child",f"{time}"])

child_count = int(sys.argv[1])

for i in range(child_count):
	child = os.fork()
	if (child > 0):
		print(f"Parent[{os.getpid()}]: I ran children process with PID {child}")
	else:
		random_t = random.randint(5,10)
		exec_child(random_t) 	

finish_num = 0
while(finish_num < child_count):
	pid, exit_status = os.wait()
	exit_status = os.waitstatus_to_exitcode(exit_status)
	print(f"Parent[{os.getpid()}]: Child with PID {pid} terminated. Exit Status {exit_status}")	
	if(exit_status != 0):
		child = os.fork()
		if (child > 0):
			print(f"Parent[{os.getpid()}]: I ran children process with PID {child}")
		else:
			random_t = random.randint(5,10)		
	else:
		finish_num = finish_num + 1			