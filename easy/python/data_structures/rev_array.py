def reversearray(a):
    
    output = []
    l = len(a)
    for i in range(l-1, -1, -1):
        output.append(a[i])
    return output

a = [2,1,4,7]
reversearray(a)
