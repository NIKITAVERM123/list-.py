# rite a code that works for any list, it should give two sums as outputs, one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.


# # Code Example
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
while i<len(elements):
    if elements[i]%2==0:
        print(elements[i],"even number")
    else:
        print(elements[i],"odd")
    i=i+1