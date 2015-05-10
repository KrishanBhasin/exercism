import collections

def numeral(arabic):
	symbols = collections.OrderedDict()
	symbols[1000]='M'
	symbols[900]='CM'
	symbols[500]='D'
	symbols[400]='CD'
	symbols[100]='C'
	symbols[90]='XC'
	symbols[50]='L'
	symbols[40]='XL'
	symbols[10]='X'
	symbols[9]='IX'
	symbols[5]='V'
	symbols[4]='IV'
	symbols[1]='I'
	
	answer = ''
	for entry in symbols:
		while arabic - entry >= 0:
			answer += symbols[entry]
			arabic -= entry

	return answer