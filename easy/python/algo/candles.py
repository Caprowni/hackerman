def candles(ar):
    max_height = 0
    candles = 0 
    for c,n in enumerate(ar):
        if c == len(ar)-1:
            if n == max_height:
                candles += 1
            return candles
        if n >= ar[c+1]:
            if n >= max_height:
                if n != max_height:
                    candles = 0
                max_height = n 
                candles += 1

#ar = [3, 1, 2, 3]
#ar = [82, 49, 82, 82, 41, 82, 15, 63, 38, 25]
#ar = [44, 53, 31, 27, 77, 60, 66, 77, 26, 36]
#candles(ar)


