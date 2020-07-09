def reverse(x):

    if x > 0:
        new_int = int(str(x)[::-1])
    else:
        new_int = -1 * int(str(x*-1)[::-1])  

    print(new_int)

x = 321
y = -123
reverse(x)
reverse(y)
