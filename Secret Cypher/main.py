# Xavier Raty Secret Cypher

alphabet = " abcdeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678910"

def decode(word):
    wordLen = len(word)
    newWord = []
    repeats = 0
    for x in word:
        letter = x 
        whereLetter = alphabet.index(letter)
        newWord.insert(repeats, alphabet[whereLetter + 1])
        word = "".join(newWord)
        repeats += 1
    print("decode",word)

decode(input("What word do you want decoded? "))