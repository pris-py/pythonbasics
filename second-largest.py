def second_largest(l):
    largest=None
    second=None
    for i in l:
        if largest is None or i>largest:
            second=largest
            largest=i
        elif i!=largest and (second is None or i>second):
            second=i
    return second            