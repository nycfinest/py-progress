import keyboard  # using module keyboard

acc1 = {
    "user": "myusername",
    "pass": "python"
}



while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('shift+pgup'):  # if key 'q' is pressed 
            print('Logged in')
            keyboard.write(acc1.get("user"))
            keyboard.press_and_release('tab')
            keyboard.write(acc1.get("pass"))
    except:
        break  # if user pressed a key other than the given key the loop will break
    
    
    
    
    

    
