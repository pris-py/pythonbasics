def count_even(l):
    c=0
    for i in l:
        if i%2==0:
            c+=1
    return c
print(count_even([1,2,3,4,5,67,7,8,9,1000]))        