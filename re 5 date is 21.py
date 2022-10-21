#n = int(input('Enter Number: '))
n = 371
n = str(n)
non = len(n)
total = 0

for i in n:
    i = int(i)
    power = i ** non
    total += power
print(total)
    


