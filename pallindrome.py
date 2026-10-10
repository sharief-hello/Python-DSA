"""
Given a string you have to find out whether the string is pallindrome or not,
if it is a pallindrome then print "PALLINDROME" and
if it is not then print "NOT PALLINDROME" 
"""

given_string = "acccba"

# Two pointers Method:

"""
First we initialize pointers on either ends of the string,
then we check first and last character to be same, 
if yes then we increase left pointer and decrease the right pointer,
to check if the next pair of characters are same,
else we know that the string is not a pallindrome,
at the end if left and right pointers are equal then we know the string was pallindrome after all
"""

left, right = 0, len(given_string) -1

while left < right :

    if given_string[left] == given_string[right]:
        left += 1
        right -=1
    else:
        print("NOT PALLINDROME")
        break
if left == right:
    print("PALLINDROME")