import string
all_letters = string.ascii_lowercase

all_numbers = [int(n) for n in '16 9 3 15 3 20 6 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14'.split()]

decoded = [all_letters[i-1] for i in all_numbers]


print(''.join(decoded))

