import time


def countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds = seconds - 1
        time.sleep(1)
        
        
if __name__ == "__main__":
    countdown(10)