def notes(*num, sit = False):
    read = len(num)
    
    mai = num[0]
    for n in num:
        if mai < n:
            mai = n
            
    mi = num[0]        
    for n in num:
        if mi > n:
            mi = n
            
    s = 0        
    for n in num:
        s += n        
    med = round(s / read, 2)
        
    data = {'Total' : read, 
    "Bigger" : mai,
    "Smaller" : mi,
    "Average" : med}
    
    if  sit == True:
        read -= 1
        if med >= 10:
            data["Situation"] = "Approved!"
        else: 
            data["Situation"] = "Failed!"  
    return data
    
res = notes(1, 4, 30, 20, sit = True)
print(res)