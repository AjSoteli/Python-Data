import csv

def convertToDictionaries(keys,values):
  newList=[]
  for aList in values:
    newDict={}
    for i in range(len(keys)):
      key=keys[i]
      value=aList[i]
      newDict[key]=value
      if newDict not in newList:
        newList.append(newDict)
  return newList

def loadRecords(filename):
  firstNewList=[]
  with open (filename) as fp:
    reader=csv.reader(fp)
    headers=next(reader)
    for line in reader:
      secondNewList=[]
      for word in line:
        if word in line:
          secondNewList.append(word)
        else:
          secondNewList.append("")
      firstNewList.append(secondNewList)
  return firstNewList

def convertToLists(keys,lod):
  firstList=[]
  for aDict in lod:
    secondList=[]
    for key in keys:
      if key in aDict:
        secondList.append(aDict[key])
      if key not in aDict:
        secondList.append("")
    firstList.append(secondList)
  return firstList

def writeRecords(filename,records):
  with open (filename, "a") as fp:
    writer=csv.writer(fp)
    for aList in records:
      writer.writerow(aList)
  return None
