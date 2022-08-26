# how to find all pairs in an array of integers whose sum is equal to the given number?
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
b=[]
while i<len(n):
    j=0
    c=[]
    while j<len(n):
        if n[i]+n[j]==30:
            c.append(n[i])
            c.append(n[j])
            b.append(c)
        j=j+1
    i=i+1
print(b)
