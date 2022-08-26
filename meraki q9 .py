# Please see this list :


# Code Example
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
sum=0
b=[]
while i<len(marks):
    if type(marks[i])==list:
        j=0
        while j<len(marks[i]):
            sum=sum+marks[i][j]
            b.append(sum)
            j=j+1
    else:
        sum=sum+marks[i]
    i=i+1
print(sum)
        