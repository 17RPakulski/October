def verifyEmail(email):
    valid = True
    
    if '@' not in email or '.' not in email or len(email) < 11:
        valid = False
  
    print(valid)
        
    
#email = input('enter: ')
verifyEmail(email = 'uagiaggg.@')