for i in range(1,151):
    print(i)

for i in range(5,1000,5):
    print(i)

for i in range(1,100):
    if i% 10 == 0:
        print("CodingDojo")
    elif i% 5 == 0:
        print("Coding")
    
    else: print(i)

sum = 0
for i in range(0,500000):
    if i%2 == 1:
        sum = sum + i
        
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,10):
    if i%mult == 0:
        print(i)