import os


fPath = 'C:\\Users\\ircho\\OneDrive\\Desktop\\pyDrill'
fName = os.listdir(fPath)
mTimes = []
testmTimes = []
aPaths= []
#abPath = os.path.join(fPath, fName)
for f in fName:
    if f.endswith('.txt'):
        nPath = os.path.join(fPath, f)
        modTime = os.path.getmtime(nPath)
        mTimes.append(modTime)
        testmTimes.append(modTime)
        aPaths.append(nPath)
testmTimes.sort()
indexes = []
for i in aPaths:
    y = 0
    index = 0
    for x in mTimes:
        
        if x == testmTimes[y]:
            index = y
            y =y +1
            indexes.append(index)
        else:
            index = index +1
counter = 0
for i in indexes:
    if counter < len(aPaths):
        print(aPaths[counter], mTimes[counter])
    counter = counter +1
