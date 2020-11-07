'''
Problem

Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits
Test Cases
Case 1

    Input: 4567
    Expected Output: 2

Explanation : Odd positions are 4 and 6 as they are pos: 1 and pos: 3, both have sum 10. Similarly, 5 and 7 are at even positions pos: 2 and pos: 4 with sum 12. Thus, difference is 12 – 10 = 2
Case 2

    Input: 5476
    Expected Output: 2

Case 3

    Input: 9834698765123
    Expected Output: 1
'''
num = input()
esum=0
osum=0
for i in range(len(num)):
	if i%2==0:
		esum+=int(num[i]) 
	else: 
		osum = int(num[i])+osum
print(osum-esum)  
