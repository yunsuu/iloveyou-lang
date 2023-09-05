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
        tokenList.append(codeText[i:endIdx+1])
        i = endIdx
    elif codeText[i] == 'L':
        endIdx = method.findEndIdxLove(codeText, i)
        tokenList.append(codeText[i:endIdx+1])
        i = endIdx
    elif codeText[i] == 'Y':
        endIdx = method.findEndIdxYou(codeText, i)
        tokenList.append(codeText[i:endIdx+1])
        i = endIdx
    elif codeText[i] == 'B':
        endIdx = method.findEndIdxBecause(codeText, i)
        tokenList.append(codeText[i:endIdx+1])
        i = endIdx
    elif codeText[i] == 'D':
        endIdx = method.findEndIdxDateWithMe(codeText, i)
        tokenList.append(codeText[i:endIdx+1])
        i = endIdx
    i+=1

print(tokenList)
