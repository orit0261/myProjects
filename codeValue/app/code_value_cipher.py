def Encrypt(message, key):
    strCode = ''
    for i in range(len(message)):
        strCode = strCode + key[i]
    return strCode


def Decrypt(message, key):
    strCode = ''
    for i in range(len(message)):
        pos = key.find(message[i].upper())
        if pos>=0:
            strchr = chr(pos+65)
        else:
             strchr=message[i]

    if message[i].islower():
              strCode = strCode + strchr.lower()
    else:
             strCode = strCode + strchr.upper()
    return strCode

    pass
