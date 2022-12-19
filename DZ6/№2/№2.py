import os 
os.chdir(r'D:\DZ_py\DZ6\№2')    #Пришлось вручную назначить директорию работы
f = open("input.txt", 'r')
coef = f.read()
f.close()
coef = coef.split("|")
print(coef)
ch = min(int(coef[0]) // 2, int(coef[1]) // 6, int(coef[2]))    
f = open('output.txt', 'w')
print(ch)
f.write(str(ch))