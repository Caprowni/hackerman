def trees(s, t, a, b, apples, oranges):

    apples_dropped = 0
    oranges_dropped = 0
    
    for n in apples:
        if a + n >= s and a +n <= t:
            apples_dropped += 1

    for n in oranges:
        if b + n >= s and b +n <= t:
            oranges_dropped += 1

    print(apples_dropped)
    print(oranges_dropped)

trees(2,3,1,5,[2],[-2])
trees(7,11,5,15,[-2,2,1],[5,-6])

