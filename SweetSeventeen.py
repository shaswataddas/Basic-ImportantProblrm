'''
Given a maximum of four digit to the base 17 (10 – A, 11 – B, 12 – C, 13 – D … 16 – G} as input, output its decimal value.
Test Cases
Case 1

    Input – 1A
    Expected Output – 27

Case 2

    Input – 23GF
    Expected Output – 10980
'''
num = str(input())
print(int(num,17))
