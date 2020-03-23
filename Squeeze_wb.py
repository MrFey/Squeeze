'''all right: Naullet Arthur'''


import argparse
import sys
import time

# PARSING:
parser = argparse.ArgumentParser(description='Creating a wordlist based on specific words',
								 epilog="An open source software create by Arthur Naullet ")
parser.add_argument('-w', '--words', help='the different words to mix up ex: -s \"word1 word2 word3\"',dest='words')
parser.add_argument('-f', '--file', help='the file for saving the wordlist (optional). Becareful, it would erase any existing file with the same name',dest='file')
parser.add_argument('-s', '--spaces', help='add spaces in your words (default: 0) must be less than the number of words',dest='spaces',nargs='?',type=int,default=0)
parser.add_argument('-u', '--upper',help='1 for adding capitalize words(default: 0)',dest="upper",nargs='?',default=False,type=int)
parser.add_argument('-m', '--max', help='define the maximum length for a word (default: the sum of the length of all words. Can not be 0) ',dest='max',nargs='?',type=int,default=0)
parser.add_argument('-r', '--rep', help='define the maximum occurance of the input words in the created word',dest='rep',nargs='?',type=int,default=1)

args = parser.parse_args()

# FUNCTIONS:
def length_of_word():
	length_of_word=0
	for i in words:
		length_of_word+=len(i)
	return length_of_word+args.spaces

def creating_wordlist(wordlist,word):
	if (len(word) > length_of_word):
		return
	if( word!="" and word[-1] != " "):
		wordlist.append(word)
	for w in words:
			if (word.count(w) < args.rep):
				creating_wordlist(wordlist,word+w)
			if (upper):
				creating_wordlist(wordlist,word+w.capitalize())
			if (word.count(" ") < args.spaces):
				creating_wordlist(wordlist,word+w+" ")

# VARIABLES:
file =  args.file
words= args.words.split(' ')
upper= args.upper
number_of_line=len(words)**len(words) # a pofiner
length_of_word=length_of_word()	
if (args.max != 0):
	length_of_word = args.max
if(args.spaces > len(words)-1):
	print "[-] Error: spaces argument must be valid "
	sys.exit()
wordlist = []

# PRINTING:
print '[+] creating words with %s characters max...' % str(length_of_word)
if(file):
	print '[+] saving the wordlist in %s...' % file
else:
	print '[+] printing the wordlist...'

time.sleep(1)

# PROGRAM
creating_wordlist(wordlist,"")
wordlist.sort()
if (file):
	f = open(file,"w")
	for w in wordlist:
		f.write(w+"\n")
	f.close()
else:
	#print "\n"
	for w in wordlist:
		print w

print '[+] process completed. %s words created.\n' % str(len(wordlist))

