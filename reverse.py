def reverse(l):
    Lnew=[]
    for i in range(len(l)-1,-1,-1):
        Lnew.append(l[i])
    return Lnew    
print(reverse([1,2,3,4,5]))        