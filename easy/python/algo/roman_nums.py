def roman_nums(s):
    
    romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    length = len(s)
    total = dic[s[n-1]]
    for i in range(length-1,0,-1):
        current = dic[s[i]]
        prev = dic[s[i-1]]
        total += prev if prev >= current else -prev
    return total

# Roman nums
#a = "III"
#d = "MCMXCIV"
#roman_nums(a)
#roman_nums(d)

