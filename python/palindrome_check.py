#string1 = input("enter a string to check palindrome:  ")
#string1 = string1.casefold()
string1 = "madm"
string2 = reversed(string1)
if list(string1) == list(string2):
    print "the given string is a palindrome"
else:
    print "the given string is not a palindrome"
