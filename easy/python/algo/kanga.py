def kangaroo(x1,v1,x2,v2):

    for _ in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

kangaroo(0,3,4,2)
kangaroo(21, 6, 47, 3)
