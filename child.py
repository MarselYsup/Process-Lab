#!/usr/bin/python3

import os 
import random
import sys
import time

print(f"child[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.")
time.sleep(int(sys.argv[1]))
print(f"Child[{os.getpid()}]: I am ended. PID {os.getpid}. Parent PID {os.getppid}.")
random_status = random.randint(0,1)
sys.exit(random_status)