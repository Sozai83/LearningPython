hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    numLength = len(hexNum)
    dec = 0
    if numLength < 4:
        for num in hexNum:
            if(num in hexNumbers):
                tempnum = hexNumbers[num]
                dec += (16 ** (numLength-1)) * tempnum
                numLength -= 1
            else:
                return None
        return dec
    
    return None


test1 = hexToDec('ZZTOP')
print(test1)

print(hexToDec('A6G'))
print(hexToDec('3C0'))