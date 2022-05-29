# CODED BY ANONPRIXOR
# CYBERMAFIA - PH
import os
import sys
from time import sleep
import sys
import requests

def logo():
	print("""

				\033[1;34;40m ██████ ██    ██ ██████  ███████ ██████  ███    ███  █████  ███████ ██  █████  
				\033[1;34;40m██       ██  ██  ██   ██ ██      ██   ██ ████  ████ ██   ██ ██      ██ ██   ██ 
				\033[1;33;40m██        ████   \033[1;37;40m██████  █████   ██████  ██ ████ ██ ███████ █████   ██ ███████ 
				\033[1;31;40m██         ██    ██   ██ ██      ██   ██ ██  ██  ██ ██   ██ ██      ██ ██   ██ 
				\033[1;31;40m ██████    ██    ██████  ███████ ██   ██ ██      ██ ██   ██ ██      ██ ██   ██ 
				                                                                               
                                                  \033[1;31;40mPH-CYBERMAFIA \033[1;37;40m| \033[1;33;40mCoded By AnonPrixor
                                                  \033[1;31;40mPlease contact me if problem persist
                                                  \033[1;32;40mhttps://www.facebook.com/profile.php?id=100081566469648     
		""")

def finder():
	os.system("clear" if os.name == "nt" else 'clear')
	logo()
	web = input("Target URL: ") # You can enable this but disable the Line 27
	#web = sys.argv[1]

	start = "CYBERMAFIA-SCANNING...\r\n"
	for s in start:
		sys.stdout.write(s)
		sys.stdout.flush()
		sleep(0.1)

	file = open("wordlist.txt", "r")
	try:
		for link in file.read().splitlines():
			curl = web + link
			res = requests.get(curl)
			if res.status_code == 200:
				print("*" * 20)
				print("\033[1;34;40mCYBERMAFIA-ADMIN FOUND -> {}".format(curl))
				print("*" * 20)
			else:
				print("\033[1;34;40mCYBERMAFIA-ADMIN NOT FOUND {}".format(curl))

	except KeyboardInterrupt:
		print("\033[1;34;40mKeyboard Request to shutdown")


	file.close()

if __name__ == "__main__":
	finder()