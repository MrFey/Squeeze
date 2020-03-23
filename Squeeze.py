import argparse
import sys
from termcolor import colored

# PARSING:
parser = argparse.ArgumentParser(description='Creating a wordlist based on specific words',
								 epilog="An open source software create by Arthur Naullet ")
parser.add_argument('-w', '--words', help='the different words to mix up ex: -s \"word1 word2 word3\"',dest='words')
parser.add_argument('-f', '--file', help='the file for saving the wordlist (optional). Becareful, it would erase any existing file with the same name',dest='file')
parser.add_argument('-s', '--spaces', help='option to add spaces in your words (default: 0) must be less than the number of words',dest='spaces',nargs='?',type=int,default=0)
parser.add_argument('-u', '--upper',help='specifying the characters where you want to try to add upper case(don\'t take in count spaces) ex : -u \"1,2,5\"',dest="uppers",nargs='?',default="")
parser.add_argument('-m', '--max', help='define the maximum length for a word (default: the sum of the length of all words) ',dest='max',nargs='?',type=int,default=0)
parser.add_argument('-r', '--rep', help='define the maximum repetition of the words in the new word',dest='rep',nargs='?',type=int,default=0)

args = parser.parse_args()

# FUNCTIONS:
def length_of_word():
	length_of_word=0
	for i in words:
		length_of_word+=len(i)
	return length_of_word+args.spaces

def creating_wordlist(wordlist,word):
	if(len(word) <= length_of_word and  word!=""):
		wordlist.append(word)
	elif(not word==""):
		return
	for w in words:
		if (w==" " and word.count(" ") < args.spaces and len(word)>0 and word[-1] != " " and len(word) <length_of_word):
			creating_wordlist(wordlist,word+w)
		elif (w != " " and word.count(w) < args.rep):
			creating_wordlist(wordlist,word+w)

def upper(string,index):
	string = list(string)
	if(string[index] == " " and index+1 <len(string)):
		index+=1
	string[index]=string[index].upper()
	res = ""
	for i in string:
		res+=i
	return res

def add_upper(wordlist):
	if(uppers==['']):
		return
	for a in uppers:
		try:
			a=int(a)
		except Exception as e:
			print colored("Error... make sure you have valide parameters","red")
			sys.exit()
	wordlist2=[]
	uppers2 = [0]*len(uppers)
	for i in range(len(uppers)): #copy
		uppers2[i] = uppers[i]

	for i in uppers:
		for w in wordlist:
			res = w
			for i2 in uppers2:
				if(int(i2)<len(res)):
					res = upper(res,int(i2))
					wordlist2.append(res)
			uppers2.insert(0,uppers2.pop()) #sliding

	wordlist.extend(wordlist2)

		

# VARIABLES:
file =  args.file
words= args.words.split(' ')
uppers= args.uppers.split(',')
number_of_line=len(words)**len(words) # a pofiner
length_of_word=length_of_word()	
if (args.max != 0):
	length_of_word = args.max
wordlist = []
for i in range(args.spaces):
	words.append(" ")

# PRINTING:
if(file):
	print 'saving the wordlist in %s...' % colored(file,'green')
else:
	print 'printing the wordlist'
print 'creating %s words of %s character max\n' % (colored("*",'green'),colored(str(length_of_word),'green'))



# PROGRAM
creating_wordlist(wordlist,"")
add_upper(wordlist)
wordlist.sort()
if (file):
	f = open(file,"w")
	for w in wordlist:
		f.write(w+"\n")
	f.close()
else:
	for w in wordlist:
		print w
print len(wordlist)

