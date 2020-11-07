key = ['break','case','continue','default','defer','else','for','func','goto','if','map','range','return','struct','type','var']
inp = input()
if inp in key:
	print(f"{inp} is a keyword")
else:
	print(f"{inp} is not a keyword")
