# Simple bookbot functions (My God, Python is annoying)

from stats import GetBookWordCount 
from stats import FakeTheResults
staticBookPath = "books/frankenstein.txt" # I understand how unhealthy this is

def GetBookContents(targetBookPath):
    with open(targetBookPath) as targetBook:
         return targetBook.read()

def main():
    currentBookContent = GetBookContents(staticBookPath)
    wordsInCurrentBook = GetBookWordCount(currentBookContent)
    # print(wordsInCurrentBook)
    FakeTheResults()
main()
