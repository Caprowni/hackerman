def minmax(a):
    all = 0
    for n in a:
        all += n
    poss = []
    for n in a:
        poss.append(all - n)
    print(min(poss), max(poss)) 

a = [1,2,3,4,5]
minmax(a)
