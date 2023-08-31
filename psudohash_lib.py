#!/bin/python3
#
# Author: Panagiotis Chartas (t3l3machus)
# https://github.com/t3l3machus

import argparse, sys, itertools

# Colors
MAIN = '\033[38;5;50m'
LOGO = '\033[38;5;41m'
LOGO2 = '\033[38;5;42m'
GREEN = '\033[38;5;82m'
ORANGE = '\033[0;38;5;214m'
PRPL = '\033[0;38;5;26m'
PRPL2 = '\033[0;38;5;25m'
RED = '\033[1;31m'
END = '\033[0m'
BOLD = '\033[1m'

# -------------- Arguments & Usage -------------- #
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawTextHelpFormatter,
	epilog='''
Usage examples:

  Basic:
      python3 psudohash.py -w <keywords> -cpa

  Thorough:
      python3 psudohash.py -w <keywords> -cpa -an 3 -y 1990-2022
'''
	)


def exit_with_msg(msg):
	parser.print_help()
	print(f'\n[{RED}Debug{END}] {msg}\n')
	sys.exit(1)



def unique(l):

	unique_list = []

	for i in l:
		if i not in unique_list:
			unique_list.append(i)

	return unique_list



_max = 51


years = ["2020","2021","2022","2023","2024"]


def banner():
	padding = '  '

	P = [[' ', '┌', '─', '┐'], [' ', '├','─','┘'], [' ', '┴',' ',' ']]
	S = [[' ', '┌','─','┐'], [' ', '└','─','┐'], [' ', '└','─','┘']]
	U = [[' ', '┬',' ','┬'], [' ', '│',' ','│'], [' ', '└','─','┘']]
	D = [[' ', '┌','┬','┐'], [' ', ' ','│','│'], [' ', '─','┴','┘']]
	O =	[[' ', '┌','─','┐'], [' ', '│',' ','│'], [' ', '└','─','┘']]
	H = [[' ', '┐', ' ', '┌'], [' ', '├','╫','┤'], [' ', '┘',' ','└']]
	A = [[' ', '┌','─','┐'], [' ', '├','─','┤'], [' ', '┴',' ','┴']]
	S = [[' ', '┌','─','┐'], [' ', '└','─','┐'], [' ', '└','─','┘']]
	H = [[' ', '┬',' ','┬'], [' ', '├','─','┤'], [' ', '┴',' ','┴']]

	banner = [P,S,U,D,O,H,A,S,H]
	final = []
	print('\r')
	init_color = 37
	txt_color = init_color
	cl = 0

	for charset in range(0, 3):
		for pos in range(0, len(banner)):
			for i in range(0, len(banner[pos][charset])):
				clr = f'\033[38;5;{txt_color}m'
				char = f'{clr}{banner[pos][charset][i]}'
				final.append(char)
				cl += 1
				txt_color = txt_color + 36 if cl <= 3 else txt_color

			cl = 0

			txt_color = init_color
		init_color += 31

		if charset < 2: final.append('\n   ')

	print(f"   {''.join(final)}")
	print(f'{END}{padding}                        by t3l3machus\n')


# ----------------( Base Settings )---------------- #
mutations_cage = []
basic_mutations = []
outfile = 'output.txt'
trans_keys = []

transformations = [
	{'a' : ['@', '4']},
	{'b' : '8'},
	{'e' : '3'},
	{'g' : ['9', '6']},
	{'i' : ['1', '!']},
	{'o' : '0'},
	{'s' : ['$', '5']},
	{'t' : '7'}
]

for t in transformations:
	for key in t.keys():
		trans_keys.append(key)



# ----------------( Functions )---------------- #
# The following list is used to create variations of password values and appended years.
# For example, a passwd value {passwd} will be mutated to "{passwd}{seperator}{year}"
# for each of the symbols included in the list below.
year_seperators = ['', '_', '-', '@']



# ----------------( Functions )---------------- #
def evalTransformations(w):

	trans_chars = []
	total = 1
	c = 0
	w = list(w)

	for char in w:
		for t in transformations:
			if char in t.keys():
				trans_chars.append(c)
				if isinstance(t[char], list):
					total *= 3
				else:
					total *= 2
		c += 1

	return [trans_chars, total]



def mutate(tc, word):

	global trans_keys, mutations_cage, basic_mutations

	i = trans_keys.index(word[tc].lower())
	trans = transformations[i][word[tc].lower()]
	limit = len(trans) * len(mutations_cage)
	c = 0

	for m in mutations_cage:
		w = list(m)

		if isinstance(trans, list):
			for tt in trans:
				w[tc] = tt
				transformed = ''.join(w)
				mutations_cage.append(transformed)
				c += 1
		else:
			w[tc] = trans
			transformed = ''.join(w)
			mutations_cage.append(transformed)
			c += 1

		if limit == c: break

	return mutations_cage



def mutations_handler(kword, trans_chars, total):

	global mutations_cage, basic_mutations

	container = []

	for word in basic_mutations:
		mutations_cage = [word.strip()]
		for tc in trans_chars:
			results = mutate(tc, kword)
		container.append(results)

	for m_set in container:
		for m in m_set:
			basic_mutations.append(m)

	basic_mutations = unique(basic_mutations)

	with open(outfile, 'a') as wordlist:
		for m in basic_mutations:
			wordlist.write(m + '\n')



def mutateCase(word):
	trans = list(map(''.join, itertools.product(*zip(word.upper(), word.lower()))))
	return trans



def caseMutationsHandler(word, mutability):

	global basic_mutations
	case_mutations = mutateCase(word)

	for m in case_mutations:
		basic_mutations.append(m)

	if not mutability:

		basic_mutations = unique(basic_mutations)

		with open(outfile, 'a') as wordlist:
			for m in basic_mutations:
				wordlist.write(m + '\n')



def append_numbering():

	global _max
	first_cycle = True
	previous_list = []
	lvl = 2

	with open(outfile, 'a') as wordlist:
		for word in basic_mutations:
			for i in range(1, lvl+1):
				for k in range(1, _max):
					if first_cycle:
						wordlist.write(f'{word}{str(k).zfill(i)}\n')
						wordlist.write(f'{word}_{str(k).zfill(i)}\n')
						previous_list.append(f'{word}{str(k).zfill(i)}')

					else:
						if previous_list[k - 1] != f'{word}{str(k).zfill(i)}':
							wordlist.write(f'{word}{str(k).zfill(i)}\n')
							wordlist.write(f'{word}_{str(k).zfill(i)}\n')
							previous_list[k - 1] = f'{word}{str(k).zfill(i)}'

				first_cycle = False
	del previous_list



def mutate_years():

	current_mutations = basic_mutations.copy()

	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for y in years:
				for sep in year_seperators:
					wordlist.write(f'{word}{sep}{y}\n')
					basic_mutations.append(f'{word}{sep}{y}')
					wordlist.write(f'{word}{sep}{y[2:]}\n')
					basic_mutations.append(f'{word}{sep}{y[2:]}')

	del current_mutations



def check_underscore(word, pos):
	if word[pos] == '_':
		return True
	else:
		return False


def append_paddings_before():

	current_mutations = basic_mutations.copy()

	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for val in common_paddings:
				wordlist.write(f'{val}{word}\n')
				if not check_underscore(val, -1):
					wordlist.write(f'{val}_{word}\n')


	del current_mutations



def append_paddings_after():

	current_mutations = basic_mutations.copy()

	with open(outfile, 'a') as wordlist:
		for word in current_mutations:
			for val in common_paddings:
				wordlist.write(f'{word}{val}\n')
				if not check_underscore(val, 0):
					wordlist.write(f'{word}_{val}\n')

	del current_mutations



def calculate_output(keyw):

	global trans_keys

	c = 0
	total = 1
	basic_total = 1
	basic_size = 0
	size = 0
	numbering_count = 0
	numbering_size = 0

	# Basic mutations calc
	for char in keyw:
		if char in trans_keys:
			i = trans_keys.index(keyw[c].lower())
			trans = transformations[i][keyw[c].lower()]
			basic_total *= (len(trans) + 2)
		else:
			basic_total = basic_total * 2 if char.isalpha() else basic_total

		c += 1

	total = basic_total
	basic_size = total * (len(keyw) + 1)
	size = basic_size

	# Words numbering mutations calc
	if True:
		global _max
		word_len = len(keyw) + 1
		first_cycle = True
		previous_list = []
		lvl = 2

		for w in range(0, total):
			for i in range(1, lvl+1):
				for k in range(1, _max):
					n = str(k).zfill(i)
					if first_cycle:
						numbering_count += 2
						numbering_size += (word_len * 2) + (len(n) * 2) + 1
						previous_list.append(f'{w}{n}')

					else:
						if previous_list[k - 1] != f'{w}{n}':
							numbering_size += (word_len * 2) + (len(n) * 2) + 1
							numbering_count += 2
							previous_list[k - 1] = f'{w}{n}'

				first_cycle = False

		del previous_list

	# Adding years mutations calc
	if True:
		patterns = len(year_seperators) * 2
		year_chars = 4
		year_short = 2
		years_len = len(years)
		size += (basic_size * patterns * years_len)

		for sep in year_seperators:
			size += (basic_total * (year_chars + len(sep)) * years_len)
			size += (basic_total * (year_short  + len(sep)) * years_len)

		total += total * len(years) * patterns
		basic_total = total
		basic_size = size

	# Common paddings mutations calc
	patterns = 2
	return [total + numbering_count, size + numbering_size]




def check_mutability(word):

	global trans_keys
	m = 0

	for char in word:
		if char in trans_keys:
			m += 1

	return m



def chill():
	pass



def derivate(words):


	global basic_mutations, mutations_cage
	keywords = []

	for w in words:
		if w.strip().isdecimal():
			exit_with_msg('Unable to mutate digit-only keywords.')

		elif w.strip() not in [None, '']:
			keywords.append(w.strip())

#	# Calculate total words and size of output
#	total_size = [0, 0]
#
#	for keyw in keywords:
#		count_size = calculate_output(keyw.strip().lower())
#		total_size[0] += count_size[0]
#		total_size[1] += count_size[1]
#
#	size = round(((total_size[1]/1000)/1000), 1) if total_size[1] > 100000 else total_size[1]
#	prefix = 'bytes' if total_size[1] <= 100000 else 'MB'
#	fsize = f'{size} {prefix}'

	open(outfile, "w").close()

	for word in keywords:
		print(f'[{GREEN}*{END}] Mutating keyword: {GREEN}{word}{END} ')
		mutability = check_mutability(word.lower())

		# Produce case mutations
		print(f' ├─ Producing character case-based transformations... ')
		caseMutationsHandler(word.lower(), mutability)

		if mutability:
			# Produce char substitution mutations
			print(f' ├─ Mutating word based on commonly used char-to-symbol and char-to-number substitutions... ')
			trans = evalTransformations(word.lower())
			mutations_handler(word, trans[0], trans[1])

		else:
			print(f' ├─ {ORANGE}No character substitution instructions match this word.{END}')

		# Append numbering
		if True:
			print(f' ├─ Appending numbering to each word mutation... ')
			append_numbering()

		# Handle years
		if True:
			print(f' ├─ Appending year patterns after each word mutation... ')
			mutate_years()

		basic_mutations = []
		mutations_cage = []
		print(f' └─ Done!')



if __name__ == '__main__':
	derivate(["maman", "papa"])
