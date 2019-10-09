#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

for sn in [64,65,66,67,68,69,70,71,72]:
	for n in range(1,255):

	# Ask for input
		remoteServer    = f"10.200.{sn}.{n}"
		remoteServerIP  = socket.gethostbyname(remoteServer)

		t1 = datetime.now()

		# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

		# We also put in some error handling for catching errors

		try:
		    for port in [22,80]:  
		        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		        sock.settimeout(0.2)
		        result = sock.connect_ex((remoteServerIP, port))
		        if result == 0:
		            print(f"\n{remoteServer} port {port}: 	 Open")
		        sock.close()

		except KeyboardInterrupt:
		    print("You pressed Ctrl+C")

		except socket.gaierror:
		    print('Hostname could not be resolved. Exiting')
		    sys.exit()

		except socket.error:
		    print("Couldn't connect to server")
		    sys.exit()

		# Checking the time again
		t2 = datetime.now()

		# Calculates the difference of time, to see how long it took to run the script
		total =  t2 - t1