# Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers and the other is the average of odd numbers from the given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
c2=0
sum=0
sum2=0
while i<len(elements):
    if elements[i]%2==0:
        print(elements[i],"even")
        c=c+1
        sum=sum+elements[i]
    else:
        print(elements[i],"odd")
        c2=c2+1
        sum2=sum2+elements[i]
    i=i+1
print(sum)
print(sum2)
print(c)
print(c2)