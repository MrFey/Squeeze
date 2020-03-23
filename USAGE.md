usage: Squeeze.py [-h] [-w WORDS] [-f FILE] [-s [SPACES]] [-u [UPPERS]]
                  [-m [MAX]] [-r [REP]]

Creating a wordlist based on specific words

optional arguments:
  -h, --help            show this help message and exit
  -w WORDS, --words WORDS
                        the different words to mix up ex: -s "word1 word2
                        word3"
  -f FILE, --file FILE  the file for saving the wordlist (optional).
                        Becareful, it would erase any existing file with the
                        same name
  -s [SPACES], --spaces [SPACES]
                        option to add spaces in your words (default: 0) must
                        be less than the number of words
  -u [UPPERS], --upper [UPPERS]
                        specifying the characters where you want to try to add
                        upper case(don't take in count spaces) ex : -u "1,2,5"
  -m [MAX], --max [MAX]
                        define the maximum length for a word (default: the sum
                        of the length of all words)
  -r [REP], --rep [REP]
                        define the maximum repetition of the words in the new
                        word

An open source software create by Arthur Naullet
