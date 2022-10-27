l = [1,2,3,4,5]

low = 0
high = len(l) -1
mid = (low + high) // 2
boolean = True


target = int(input('Enter: '))
while boolean:
    if l[mid]== target:
        print( mid)
    elif l[mid] < target:
        low = mid + 1     
    else:
        high = mid - 1
        
    if low > high:
        boolean = False
    
    print( -1)
    

