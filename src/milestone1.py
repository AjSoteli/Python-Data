def getValuesForKey(key,records):
    newList=[]
    for aDict in records:
        if key in aDict:
            value=aDict[key]
            if value not in newList:
                newList.append(value)
    return newList

def countMatchesByKey(key,value,records):
    total=0
    for aDict in records:
        if key in aDict and aDict[key] == value:
            total=total+1
    return total

def countMatchesByKeys(key1,value1,key2,value2,records):
    total=0
    for aDict in records:
        if key1 in aDict and aDict[key1]==value1 and key2 in aDict and aDict[key2]==value2:
            total=total+1
    return total

def filterByKey(key,value,records):
    newList=[]
    for aDict in records:
        if key in aDict and aDict[key]==value:
            newList.append(aDict)
    return newList

def computeFrequency(key,records):
    newDict={}
    for aDict in records:
        if key in aDict:
            info=aDict[key]
            if info not in newDict:
                newDict[info]=1
            else:
                newDict[info]=newDict[info]+1
    return newDict
