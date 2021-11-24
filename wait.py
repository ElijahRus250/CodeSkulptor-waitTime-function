import time
def wait(x):
    t = time.time()
    while True:
        if str(time.time() - t).startswith(str(x)):
            break
            
            
'''
Simple Usage:
print('Hello!')
wait(5)
print('Hello but delayed!')
'''
