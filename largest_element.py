def largest(l):
    big=l[0]
    for i in range(l):
        if i>big:
            big=i
    return big 
print(largest([1,2,3,48,4]))
