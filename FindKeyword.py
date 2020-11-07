'''
One programming language has the following keywords that cannot be used as identifiers:

break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var

Write a program to find if the given word is a keyword or not
Test cases
Case 1

    Input – defer
    Expected Output – defer is a keyword

Case 2

    Input – While
    Expected Output – while is not a keyword
'''
key = ['break','case','continue','default','defer','else','for','func','goto','if','map','range','return','struct','type','var']
inp = input()
if inp in key:
	print(f"{inp} is a keyword")
else:
	print(f"{inp} is not a keyword")
