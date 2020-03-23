import argparse
import sys
from termcolor import colored

# PARSING:
parser = argparse.ArgumentParser(description='Creating a wordlist based on specific words',
								 epilog="An open source software create by Arthur Naullet ")
parser.add_argument('-w', '--words', help='the different words to mix up ex: \"word1 word2 word3\"',dest='words')
parser.add_argument('-f', '--file', help='the file for saving the wordlist (optional). Becareful, it would erase any existing file with the same name',dest='file')
parser.add_argument('-s', '--spaces', help='option to add spaces in your words (default : 0) must be less than the number of words',dest='spaces',nargs='?',type=int,default=0)
args = parser.parse_args()

# FUNCTIONS:
def length_of_word():
	length_of_word=0
	for i in words:
		length_of_word+=len(i)
	return length_of_word+args.spaces

def creating_wordlist(wordlist,word):
	if(len(word)>=length_of_word):
		if(1):
			wordlist.append(word)
		return
	for w in words:
		if (w==" " and word.count(" ") < args.spaces and len(word)>0 and word[-1] != " " and len(word) <length_of_word-1):
			creating_wordlist(wordlist,word+w)
		elif (w not in word and w != " "):
			creating_wordlist(wordlist,word+w)

		

# VARIABLES:
file =  args.file
words= args.words.split(' ')
number_of_line=len(words)**len(words) # a pofiner
length_of_word=length_of_word()	
wordlist = []
for i in range(args.spaces):
	words.append(" ")

# PRINTING:
if(file):
	print 'saving the wordlist in %s...' % colored(file,'green')
else:
	print 'printing the wordlist'
print 'creating %s words of %s character each\n' % (colored(str(number_of_line),'green'),colored(str(length_of_word),'green'))



# PROGRAM
creating_wordlist(wordlist,"")
if (file):
	f = open(file,"w")
	for w in wordlist:
		f.write(w+"\n")
	f.close()
else:
	for w in wordlist:
		print w


