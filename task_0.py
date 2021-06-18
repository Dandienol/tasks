import random
random.seed()

mist1=[]
mist2=[]
maxim=-101
seq=0
ab=0

for i in range (30):
    mist1.append(random.randint(-100,100))

print("Список випадкових чисел: \n")

mist3 = [mist1[i:i + 10] for i in range(0,len(mist1), 10)]

for i, e in enumerate(mist3, 10):
    print(e)
    
for num in mist1:
    seq+=1
    if num>maxim:
        maxim=num
        ab=seq
        
print ("\n","Максимальне зі списку:",maxim,"його порядковий номер",ab)

print("Від'ємні числа , що стоять поруч: \n")

for i in range (len(mist1)-1):
    if mist1[i]<0 and mist1[i+1]<0 :
        print (mist1[i], mist1[i+1])
