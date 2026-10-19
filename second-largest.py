def second_largest(l):
    largest=None
    second=None
    for i in l:
        if largest is None and i>largest:
            largest=i
        elif i<largest and (second is None or i>second):
            second=i
    return second            

def seclarge(L):
    first= None
    second= None
    for i in L:
        if first is None or i>first:
            second=first
            first=i
        elif i!=first and (second is None or i>second):
            second=i
    return second    