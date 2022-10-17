fo = open('//lwetb-acc-fs01/StudentUserData$/17RPakulski.ACC/Documents/text.txt', 'r')


a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listt =[]


userk = int(input('Enter Key: '))
print('--------------------------------------------------------')

print('\nEncrypted')
for line in fo:
    for item in line:
        if item == ' ':
            print('\n')
            listt.append('\n')
        else:
            hehe = (a[a.index(item)+userk])
            print (hehe)
            listt.append(hehe)
fo.close()
fo = open('//lwetb-acc-fs01/StudentUserData$/17RPakulski.ACC/Documents/text.txt', 'r')

print('--------------------------------------------------------')

print('Decrypted')


for item in listt:
    if item == '\n':
        print('\n')
    else:
        print(a[a.index(item) - userk])
    

