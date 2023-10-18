import random

servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'
    

# Your code here!
def getWithRetry(dataFunc):
    count = 0
    while servicesAreUp and count < 100:
        dataFunc()
        count += 1

getWithRetry(getData50)

def getWithRetry(dataFunc):
    maxRetry = 0
    for _ in range(0, maxRetry):
        response = dataFunc()
        if response:
            return response
        

def someFunc(var1, var2, var3, var4):
    return(var1, var2, var3, var4)

someFunc(var1=1, var2=2, var3=3, var4=4)