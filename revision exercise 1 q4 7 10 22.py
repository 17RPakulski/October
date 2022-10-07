run = True
count = 0
l = []
total = 0

while run:
    u = int(input('Enter a digit: '))
    
    if u == 0:
        break
    
    else:
        l.append(u)
        count += 1
        
for i in l:
    total += i
    mean = total/count
    

print('\nAverage of all num =',mean)




    

        
    
    