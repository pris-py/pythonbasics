def smallest(l):
    s=l[0]
    for i in l:
        if i<s:
            s=i
    return s