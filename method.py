def findEndIdxI(str, idx):
    if str[idx] != 'I':
        return -1
    endIdx = idx
    return endIdx

def findEndIdxLove(str, idx):
    if str[idx] != 'L':
        return -1
    endIdx = idx + 3
    return endIdx

def findEndIdxYou(str, idx):
    if str[idx] != 'Y':
        return -1
    endIdx = idx + 2
    return endIdx

def findEndIdxBecause(str, idx):
    if str[idx] != 'B':
        return -1
    endIdx = idx + 6
    return endIdx

def findEndIdxDateWithMe(str, idx):
    if str[idx] != 'D':
        return -1
    endIdx = idx + 11
    return endIdx

def findEndIdxHeyIHaveSomethingToTellYou(str, idx):
    if str[idx] != 'H':
        return -1
    endIdx = idx + 32
    return endIdx

def findEndIdxWouldYouLikeYoBeMyGirlfriend(str, idx):
    if str[idx] != 'W':
        return -1
    endIdx = idx + 34
    return endIdx