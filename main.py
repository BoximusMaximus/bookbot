

def GetBookText(targetBookPath):
    with open(targetBookPath) as targetBook:
         contents = targetBook.read()
    return contents

def main():
    print(GetBookText("books/frankenstein.txt"))

main()
