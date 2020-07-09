def clouds(c):
    
    hops = 0
    i = 0 
    while i < len(c)-1:
        if i < len(c)-2 and c[i+2] != 1:
            i += 1
        hops +1
        i +=1
    return hops 


c = [0,0,1,0,0,1,0]
clouds(c)
