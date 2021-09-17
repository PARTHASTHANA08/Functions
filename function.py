def wordCount():
    fileName = input("Enter The File Name : ")

    numberOfWords = 0
    file = open(fileName, 'r')
    for line in file:
       word = line.split() 
       numberOfWords = numberOfWords + len(word)

    print("Number Of Words : ")
    print(numberOfWords)   

wordCount()    