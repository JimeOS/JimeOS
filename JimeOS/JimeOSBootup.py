import os
import sys
import time
import random
import smtplib
from Information import *

#SERVER = "localhost"

print ("\nJimeOS booting, please wait...")
time.sleep(3)
login = input("\nEnter your JimeOS username: ")

# Change from guest to own username!
if login == 'Guest':
	usrpass = input ("Enter your password: ")
	# Change password to own password!
	if usrpass == '':
		print ("									  ")
		print ("   ___ _                 _____ _____  ")
		print ("  |_  (_)               |  _  /  ___| ")
		print ("    | |_ _ __ ___   ___ | | | \ `--.  ")
		print ("    | | | '_ ` _ \ / _ \| | | |`--. \ ")
		print ("/\__/ / | | | | | |  __/\ \_/ /\__/ / ")
		print ("\____/|_|_| |_| |_|\___| \___/\____/  ")
		print ("									  ")
		print ("\n\n")
		def CommandLine():
			command = input("Please enter a command: ")
			if command == 'Logoff':
				print ("Logging of...")
				time.sleep(2)
				print ("Goodbye...")
				exit(1)
		
			if command == 'Sleep':
				print ("Putting to sleep...")
				time.sleep(2)
				print ("Goodnight...")
				wake = input("")
				if wake == '':
					print ("Waking up...\n")
					time.sleep(2)
					CommandLine()
					
			if command == 'Info':
				print ("Loading all JimeOS profiles...")
				Info()
				time.sleep(1)
				print("\n")
				CommandLine()

pass
CommandLine()