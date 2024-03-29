#! /usr/bin/env python3
#-- all rights: @fey --#
#-- py-version: 3.*  --#


import argparse
import sys
import time
import os
from psudohash_lib import derivate
from termcolor import colored

# PARSING:
parser = argparse.ArgumentParser(description='Creating a wordlist based on specific words',
								 epilog="An open source software create by @Fey and pseudohash from @t3l3machus")
parser.add_argument('-w', '--words', help='the different words to mix up ex: -w \"word1 word2 word3\"',dest='words')
parser.add_argument('-f', '--file', help='the file for saving the wordlist (optional). Becareful, it would erase any existing file with the same name',dest='file')
parser.add_argument('-s', '--spaces', help='add spaces in your words (default: 0) must be less than the number of words',dest='spaces',nargs='?',type=int,default=0)
parser.add_argument('-m', '--max', help='define the maximum length for a word (default: the sum of the length of all words. Can not be 0) ',dest='max',nargs='?',type=int,default=0)
#parser.add_argument('-r', '--rep', help='define the maximum occurance of the input words in the created word',dest='rep',nargs='?',type=int,default=1)
parser.add_argument('-S', '--strict', help='precise the exact length of the words including spaces',dest='strict',nargs='?',type=int,default=0)
parser.add_argument('-d', '--derivation', help='based on psudohash project, derivate the words',dest='derivation',nargs='?',type=int,default=0)


args = parser.parse_args()

if (not args.words):
	print(colored("[-]","red"),"Error: list of words is null")
	exit()

# FUNCTIONS:
def length_of_word():
	if (args.strict):
		#print "len :",args.strict
		return args.strict
	length_of_word=0
	for i in words:
		length_of_word+=len(i)
	return length_of_word+args.spaces

def creating_wordlist(wordlist,word,i):
	if (len(word) > length_of_word):
		return
	if(((args.strict != 0 and len(word)==args.strict) or args.strict==0) and word!="" and word[-1] != " "):
		wordlist.append(word)
	for w in words:
		if (word.count(w) < args.rep):
			creating_wordlist(wordlist,word+w,-1)
		if (upper and not is_number(w)):
			creating_wordlist(wordlist,word+w.capitalize(),-1)
		if (word.count(" ") < args.spaces):
			creating_wordlist(wordlist,word+w+" ",-1)
		if (i>=0):
			i+=1
			sys.stdout.write("\033[F")
			print('['+colored('+','light_green', attrs=["bold"])+"] status: "+str(i*100//len(words)),"%")
			#time.sleep(1)

def is_number(str):
	try:
		int(str)
	except ValueError:
		return False
	return True

if __name__ == "__main__":
	# VARIABLES:
	file =  args.file
	words= args.words.split(' ')
	#upper= args.upper
	upper = 0
	number_of_line=len(words)**len(words) # a pofiner
	length_of_word=length_of_word()
	if (args.max != 0):
		length_of_word = args.max
	if(args.spaces > len(words)-1):
		print('['+colored('-','red')+"] Error: %s argument must be valid " % colored("spaces","red"))
		sys.exit()
	wordlist = []

	# PRINTING:
	if (args.strict != 0):
		print('['+colored('+','light_green', attrs=["bold"])+'] creating words with %s characters ...' % colored(str(args.strict),'light_green', attrs=["bold"]))
	else:
		print('['+colored('+','light_green', attrs=["bold"])+'] creating words with %s characters max...' % colored(str(length_of_word),'light_green', attrs=["bold"]))
	if(file):
		print('['+colored('+','light_green', attrs=["bold"])+'] saving the wordlist in %s...\n' % colored(file,'light_green', attrs=["bold"]))
	else:
		print('['+colored('+','light_green', attrs=["bold"])+'] printing the wordlist...\n')

	time.sleep(1)

	# PROGRAM
	args.rep =1 # waiting for rep arg to be fix ^^
	creating_wordlist(wordlist,"",0)
	wordlist.sort()
	if (not args.derivation):
		print('['+colored('+','light_green', attrs=["bold"])+'] starting derivation...\n')
		derivate(wordlist)
		wordlist = open("output.txt").read().split("\n")
		os.remove("output.txt")
	if (file):
		f = open(file,"w")
		for w in wordlist:
			f.write(w+"\n")
		f.close()
	else:
		#print "\n"
		for w in wordlist:
			print(w)

	print('['+colored("+","light_green", attrs=["bold"])+'] process completed. %s words created.\n' % colored(str(len(wordlist)),'light_green', attrs=["bold"]))

