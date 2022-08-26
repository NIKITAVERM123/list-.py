# this program, if we are given any number in binary form, then we will learn to convert that number in decimal form.

# content
# Please see this diagram.
binary_number = [1, 0, 0, 1, 1, 0, 1, 1,1,2]
i=-1
b=0
sum=0
while i>-len(binary_number):
    sum=sum+ binary_number[i]*2**b
    b=b+1
    i=i-1
print(sum)

