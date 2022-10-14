fo = open('C:/Users/17RPakulski.ACC/Downloads/onTime (1).txt', 'r')
l = []
l2 = []
frequency = 0


for line in fo:
    for item in line.strip('\n').split(' '):
        
        if item=='':
            pass
        
        else:
            l.append(item)


for i in l:
    if i in l2:
        l2.append(i)
        pass
    else:
        print('Frequency of', i, '=',l.count(i))

    
    
