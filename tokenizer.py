import method

codeText = ''
with open('code.txt', 'r') as code_file:
    codeText = code_file.read()
    # for line in code_file:
    #     print(line)


# print(codeText)

i = 0
tokenList = []
while i < len(codeText):
    if codeText[i] == 'I':
        endIdx = method.findEndIdxI(codeText, i)
        tokenList.append(["KEYWORD", codeText[i:endIdx+1]])
        i = endIdx
    elif codeText[i] == 'L':
        endIdx = method.findEndIdxLove(codeText, i)
        tokenList.append(["KEYWORD", codeText[i:endIdx+1]])
        i = endIdx
    elif codeText[i] == 'Y':
        endIdx = method.findEndIdxYou(codeText, i)
        tokenList.append(["KEYWORD", codeText[i:endIdx+1]])
        i = endIdx
    elif codeText[i] == 'B':
        endIdx = method.findEndIdxBecause(codeText, i)
        tokenList.append(["KEYWORD", codeText[i:endIdx+1]])
        i = endIdx
    elif codeText[i] == 'D':
        endIdx = method.findEndIdxDateWithMe(codeText, i)
        tokenList.append(["KEYWORD", codeText[i:endIdx+1]])
        i = endIdx
    elif codeText[i] == 'H':
        endIdx = method.findEndIdxHeyIHaveSomethingToTellYou(codeText, i)
        tokenList.append(["KEYWORD", codeText[i:endIdx+1]])
        i = endIdx
    elif codeText[i] == 'W':
        endIdx = method.findEndIdxWouldYouLikeYoBeMyGirlfriend(codeText, i)
        tokenList.append(["KEYWORD", codeText[i:endIdx+1]])
        i = endIdx
    elif codeText[i] == '.' or codeText[i] == ',':
        startIdx = i
        while(True):
            if codeText[i] == '.' or codeText[i] == ',':
                i+=1
            else:
                break
        endIdx = i-1
        i-=1
        tokenList.append(["CONSTANT", codeText[i:endIdx+1]])
    else:
        if codeText[i] != '\n':
            tokenList.append(["SYMBOL", codeText[i]])

    i+=1

for token in tokenList:
    print(token)
