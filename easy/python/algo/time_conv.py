def timeconversion(s):
   
    times = {"01": "13", "02": "14", "03": "15", "04":"16", 
            "05": "17", "06": "18", "07": "19", "08":"20",
            "09":"21","10":"22","11":"23","12": "00"}
   
    new_time = ""
    leading_time = ""
    time = s.split(":")
            
    for z in time:
        if "PM" in z and time[0] == "12":
            time[0] = time[0]
        elif "AM" in z and time[0] == "12" or "PM" in z:
            time[0] = times[time[0]]
        else:
            time[0] = time[0]
        
    for n in time:
        new_time += n+":"
    return new_time[:-3]

s = "03:10:12AM"
v = "12:00:21AM"
r = "12:45:54PM"
timeconversion(r)
timeconversion(s)
timeconversion(v)

