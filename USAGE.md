usage: Squeeze.py [-h] [-w WORDS] [-f FILE] [-s [SPACES]] [-u [UPPER]]
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
                        add spaces in your words (default: 0) must be less
                        than the number of words
  -u [UPPER], --upper [UPPER]
                        1 for adding capitalize words(default: 0)
  -m [MAX], --max [MAX]
                        define the maximum length for a word (default: the sum
                        of the length of all words. Can not be 0)
  -r [REP], --rep [REP]
                        define the maximum occurance of the input words in the
                        created word

An open source software create by Arthur Naullet