def grades(arr):
    
    final_grades = []
    for n in arr:
        if n >= 38:
            if n % 5 >= 3:
                n += (5 - n % 5)
        final_grades.append(n)
    return final_grades

arr = [4, 73, 67, 38, 33]
grades(arr)
