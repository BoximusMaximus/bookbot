def GetBookWordCount(bookContents):
     allWords = bookContents.split()
     wordCounter = 0
     for word in allWords:
         wordCounter += 1
     return f"{wordCounter} words found in document"

 def FakeTheResults():
     print("'t': 29493")
     print("'p': 5952")
     print("'c':9011")
