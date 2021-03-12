def security(auth):
    
    authenticate = False
    
    while(authenticate == False):
        
        guess = input("What is your name?\t")
    
        for i in range(len(auth)):
            if auth[i] == guess:
                authenticate = True
            else:
                continue
        
        if guess in auth:
            print(f"Welcome {guess}!")
            authenticate = True
        else:
            print("Imposter")