import time
X = 5
print(X)
X = X**5
print(X)
if X<10:
    print("our number X is a small value")
elif X<100:
    print("The number is an average value")
else:
    print("the number holds a big value")
counter = 0
for counter in range(0, 100,5):
    print(counter)
    time.sleep(.25)
counter = 0
while counter < X:
    print(counter*5)
    time.sleep(.25)
    if(counter<1):
        counter = 1;
    counter = counter *5
dictionary={'orange':'Fruit','milk':'dairy','carrots':'vegitable'}
print(dictionary)
dictionary['chicken']='Poltry'
print(dictionary)
