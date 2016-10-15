#!/usr/bin/env python 3

import operator



operators = {
	'+' : operator.add,
	'-' : operator.sub,
	'*' : operator.mul,
	'/' : operator.truediv,
	'^' : pow
}

def calculate(string):
	stack = list()

	for token in string.split():
		try:
			token = float(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			stack.append(function(arg1, arg2))

		print(stack)


	if(len(stack) != 1):
		raise TypeError("Too many params")

	return stack[0]
	

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()
