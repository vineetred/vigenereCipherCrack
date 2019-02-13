from collections import Counter

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#From the Oxford Math Centre
letterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
#Enter cipher text here!!!!!!!
cipher_text = "hdsfgvmkoowafweetcmfthskucaqbilgjofmaqlgspvatvxqbiryscpcfrmvswrvnqlszdmgaoqsakmlupsqforvtwvdfcjzvgsoaoqsacjkbrsevbelvbksarlscdcaarmnvrysywxqgvellcyluwwveoafgclazowafojdlhssfiksepsoywxafowlbfcsocylngqsyzxgjbmlvgrggokgfgmhlmejabsjvgmlnrvqzcrggcrghgeupcyfgtydycjkhqluhgxgzovqswpdvbwsffsenbxapasgazmyuhgsfhmftayjxmwznrsofrsoaopgauaaarmftqsmahvqecev"

#This function decrypts a given cipher text when supplied with the key
def decrypt(cipherText, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in cipherText]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

#This function breaks down the text such that the letters after
#every succesive keyLength gap are put into one array
def breakText(size, keySize):
    text_list = list(cipher_text)
    text_list = text_list[size::keySize]
    return text_list

#This is our main cracking function
def vigenereCrack(keySize):
    keys = []
    for tries in range(keySize):
        keySize = tries+1
        #The possible key is initialised as an empty string
        possibleKey = ''
        #We do not know the key length size. So we try a range from 0 to keySize
        for hell in range(keySize):
            scoreArr = []
            #Iterate through all letters to find the most appropriate subkey
            for letter in letters:
                score = 0
                #This breaks down the text by calling breakText
                subText = breakText(hell,keySize)
                #We decrypt it using some letter
                subDecrypt = decrypt(subText, letter)
                #Then we analyse it's frequency
                subFrequency = Counter(subDecrypt)
                #We calculate the score of this decyrpted text
                for index in letterFreq:
                    subScore = subFrequency[index]*letterFreq[index]
                    score+=subScore
                #We append the score to an array
                scoreArr.append(score)
            #After all possible subkeys are tried, we find the letter with the maximum score
            maximum = letters[scoreArr.index(max(scoreArr))]
            #We append that to our possible key
            possibleKey+=str(maximum)
        #We save all these keys in one array and then return it to be decrypted on the original text
        keys.append(possibleKey)
    return keys

keyLength = input("Enter max key length: ")
keys = vigenereCrack(int(keyLength))
for key in keys:
    print("\nKey: ", key, " Length: ",len(key))
    print(decrypt(cipher_text,key))