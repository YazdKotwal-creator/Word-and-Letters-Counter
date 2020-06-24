introString = input("Enter your introduction:")
charactercount = 0
wordcount = 1
for i in introString:
    charactercount=charactercount+1

    if(i==' '):
        wordcount=wordcount+1
        print("Number of words:")
        print (wordcount)
        print("Number of characters in the string")
    print(charactercount)
print (introString)