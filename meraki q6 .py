# alindrome is a word, sentence, verse, or even a number that reads the same backward or forward. Like NITIN. Read Nitin either from left or right, it will be same. Similarly MOM is also a palindrome.

# Write a code that checks whether a list is a palindrome or not. And print “Haan! palindrome hai” if its a pallindrome and “nahi! palindrome nahi hai” if its not a palindrome.

# For the time being you can use the list given below for writing the code.
a=[2,3,2]
i=0
rev=1
while i<len(a) and rev<=len(a):
    b=a[i]
    c=a[-rev]
    i=i+1
    rev=rev+1
if b==c:
    print("polidaorm number")
else:
    print("not")
sclicing
name=["m","o","m"]
rev=(name[::-1])
if rev==name:
    print("polidar")
else:
    print("not")