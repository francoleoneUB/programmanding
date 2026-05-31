def alfabetica(word):
    word = word.lower()
    wordArray = list(word)

    for i in range(len(wordArray)-1):
        if ord(wordArray[i]) > ord(wordArray[i+1]):
            return False
        
    return True

print(alfabetica("palabra"))