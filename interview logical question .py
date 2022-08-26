a=[1,4,9,0,5,12,2]
i=0
sum=0
b=[]
while i<len(a):
    if a[i]%2==0:
        sum=sum+a[i]
    i=i+1
print(sum)
a=[2,3,4,2,[3,4,5],5,66,5]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type (a[i][j]):
                b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)
a=[10,20,30,40,50]
i=0
b=[]
while i<len(a):
    while a[i]>0:
        if a[i]%10!=0:
            b.append(a[i])
            break
        a[i]//=10
    i=i+1
print(b)
a=["nikita"]
i=0
c=[]
d=5
while i<len(a[0]):
    print(a[0][i],end="")
    print(d,end="")
    d=d+5
    i=i+1
a=[102,104,105,106,107]
i=0
s=[]
while i<len(a):
    k=str(a[i])
    f=""
    y=""
    j=0
    while j<len(k):
        if k[j]!="0":
            f=f+k[j]
        else:
            y=y+k[j]
        j=j+1
    s.append(int(f+y))
    i=i+1
print(s)
a=[[12],[12,13,13],[12,34]]
i=0
max=0
c=0
while i<len(a):
    b=len(a[i])
    if max<b:
        c=a[i]
    max=max+1
    i=i+1
print(max,c)