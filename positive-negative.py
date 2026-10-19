def count(L):
    positive=0
    negative=0
    for i in L:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
    print("positive numbers:",positive)
    print("negative numbers:",negative)            