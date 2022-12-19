def cod(a):
    for i in range(len(a)):
        a[i] = list(a[i])
        
    for i in a:
        for j in range(len(i)):
            i[j] = ord(i[j])
            
    return a

def decode(a):
    for i in range(len(a)):
        a[i] = str(bytes(a[i]))[2:-1]
    
    return a
            
            
l = ['dima', 'codes', 'bytes']
 
cod(l)
print(*l)

decode(l)
print(*l)