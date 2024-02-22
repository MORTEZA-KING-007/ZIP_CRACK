#!/usr/bin/python2.7
import os
import sys
import random
import time
import zipfile
import datetime

pwx = []
u = []
def crack():
	INPUT = raw_input("\033[1;32mENTER YOUR ZIP FILE PATH => ")
	file = "{}".format(INPUT)
	
	f = zipfile.ZipFile(file)
	
	PUT = raw_input("\033[1;32mENTER YOUR ZIP FILE PASSWORD PATH => ")
	pd = "{}".format(PUT)
	print "\033[1;37m============================================="
	
	for line in open(pd, 'r').readlines():
		pwx.append(line.strip())
	
	for ps in pwx:
		try:
			f.extractall(pwd=ps)
			print "\033[1;32mCORRECT PASSWORD : ", ps
			u = os.listdir("./")
			for file_name in u:
				if file_name == "crack.py":
					pass
				elif file_name == "unzip.py":
					pass
				else:
					new_name = "unzipped_by_morteza.{}".format(file_name)
					os.rename(file_name, new_name)
					os.system("mv {} /sdcard".format(new_name))
			break
		except:
			pass
	
	print "\033[1;37m============================================="
if __name__ == "__main__":
	crack()

