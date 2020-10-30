'''
The program will recieve 3 English words inputs from STDIN

    These three words will be read one at a time, in three separate line
    The first word should be changed like all vowels should be replaced by %
    The second word should be changed like all consonants should be replaced by #
    The third word should be changed like all char should be converted to upper case
    Then concatenate the three words and print them

Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h%wa#eYOU.

You can assume that input of each word will not exceed more than 5 chars
'''

even = ["a","e","i","o","u"]
odd = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

a = input("First: ")
b = input("Second: ")
c = input("Third: ")
for i in range(len(even)-1):
    a = a.replace(even[i],"%")
for i in range(len(odd)-1):
    b = b.replace(odd[i],"@")
c=c.upper()
print(a+b+c)
