import os
import json

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

def encodeFile(filename, newFilename):
    newLines = ''
    with open(filename, 'r') as f:
        lines = f.readlines()
        newLines = encodeString(lines)

    with open(newFilename, 'w') as f:
        f.write(json.dumps(encodeString(lines)).strip())

def decodeFile(filename):
    pass

print(f'Original file size: {os.path.getsize("10_04_challenge_art.txt")}')

encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

print(f'New file size: {os.path.getsize("10_04_challenge_art_encoded.txt")}')

decodeFile('10_04_challenge_art_encoded.txt')