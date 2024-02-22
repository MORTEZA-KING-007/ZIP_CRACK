#by the name of allah
#totally coded by morteza alizadeh
#!/usr/bin/python3.11
import os
import sys
import time
import base64
import zipfile
import random
import datetime
import platform
import colorama
from datetime import datetime
from colorama import Fore,Style
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
CYAN = Fore.CYAN
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
BLACK = Fore.BLACK
morteza = "owner"
#------List
NULL = "NULL"
pwx = []

def simple_zip():
	try:
		clear()
		INPUT = input(f'{GREEN}[✓] ENTER YOUR ZIP FILE PATH ➟ ')
		file = f'{INPUT}'
		zip = zipfile.ZipFile(file)
		zip.extractall()
		print(f'\n\t\t{WHITE}[💎]{GREEN} FILE DECOMPRESSED SUCCESSFULLY ..!')
		u = os.listdir("./")
		for file_name in u:
			if file_name == "crack.py":
				pass
			elif file_name == "unzip.py":
				pass
			else:
				new_name = f"unzipped_by_morteza.{file_name}"
				os.rename(file_name, new_name)
				os.system(f"mv {new_name} /sdcard")
		input(f"\n{GREEN}PRESS ENTER TO RETURN MAIN MENU ××> ");main();
	finally:
		print(f'\n\t\t{WHITE}[💎]{RED} FILE  NOT DECOMPRESSED SUCCESSFULLY ..!')
		input(f"\n{GREEN}PRESS ENTER TO RETURN MAIN MENU ××> ");main();


def hard_zip():
	#it will code with python2.7
	os.system("clear")
	print(log)
	os.system("python2 crack.py")
	input(f"\n{GREEN}PRESS ENTER TO RETURN MAIN MENU ××> ");main();
	
	
def clock():
	try:
		current = datetime.now()
		hour = current.hour
		minute = current.minute
		year = current.year
		month = current.month
		Time = f'{GREEN}{year}/{month}{MAGENTA} ~> {GREEN}{hour}:{minute}'
		return Time
	except:
		return False

def bitch():
	b = platform.architecture()[0]
	if b in ["64", "64bit"]:
		tag = "64 BIT"
		return tag
	elif b in ["32", "32bit"]:
		tag = "32 BIT"
		return tag
	else:
		return NULL


def clear():
	try:
		os.system("clear")
		os.system("echo -e '\e[1;32m'")
		os.system("toilet -f slant UNZIP_TOOL")
		print(Fore.GREEN, log)
	except:
		return False


def liner():
	print(f'{WHITE}===============================================')


log = f"""
\033[1;32m╔\033[1;32m𓆩M𓆪\033[1;32m═══════════════════[\033[37;41m𝐌.𝐀✯𝐓𝐄𝐀𝐌\033[0m\033[1;32m]═════════════════\033[1;32m𓆩M𓆪\033[1;32m╗
\033[1;32m│\033[1;37m☞  \033[1;32mAUTHER     \033[1;37m➟   \033[1;32mMORTEZA ALIZADEH                  \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mFACEBOOK   \033[1;37m➟   \033[1;32mMORTAZA ALIZADEH                  \033[1;32m│
\033[1;32m│\033[1;37m☞  \033[1;32mGITHUB    \033[1;37m ➟  \033[1;32m mortazanafas                     \033[1;32m │
\033[1;32m│\033[1;37m☞  \033[1;32mVERSION   \033[1;37m ➟   \033[1;32m3.0                            \033[1;32m   │
\033[1;32m│\033[1;37m☞  \033[1;32mDEVICE BIT\033[1;37m ➟   \033[1;32m{bitch()}                         \033[1;32m   │
\033[1;32m│\033[1;37m☞  \033[1;32mTIME &DATE\033[1;37m ➟   \033[1;32m{clock()}               \033[1;32m   │
\033[1;32m╚\033[1;32m𓆩M𓆪\033[1;32m═════\033[41m\033[1;37m[ 𓆩𝐈𝐟 𝐘𝐨𝐮𝐫 𝐁𝐚𝐝 𝐒𝐨 𝐈 𝐚𝐦 𝐘𝐨𝐮𝐫 𝐃𝐚𝐝𓆪 ]\033[0m\033[1;32m═══════\033[1;32m𓆩M𓆪\033[1;32m╝
"""


def main():
	clear()
	liner()
	print(33 * f"{WHITE}=")
	print(f'{WHITE}[{YELLOW}01{WHITE}]{WHITE} UNZIP SOME ZIP FILE')
	print(f'{WHITE}[{YELLOW}02{WHITE}]{WHITE} CRACK SOME ZIP FILE PASSWORD')
	print(f'{WHITE}[{YELLOW}00{WHITE}]{RED} EXIT FROM PROGRAM')
	print(33 * f"{WHITE}=")
	king = input(f'{GREEN}[✓] CHOOSE ➟ ')
	if king in ["01", "1"]:
		simple_zip()
	elif king in ["02", "2"]:
		hard_zip()
	elif king in ["00", "0"]:
		os.system("clear")
		sys.exit(f'\n\t[💞] PROJECT BY MORTEZA ALIZADEH [💞]')
	else:
		return main()
#--------------------------------------#
if morteza == "owner":
	main()
