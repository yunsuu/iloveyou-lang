def writePush(r, n):
    result=''
    resultScope = r
    if r == 'CONST':
        resultScope = 'constant'
    if r == 'ARG':
        resultScope = 'argument'
    if r == 'var':
        resultScope = 'local'
    if r == 'STATIC':
        resultScope = 'static'
    if r == 'THIS' or r =='field':
        resultScope = 'this'
    if r == 'THAT':
        resultScope = 'that'
    if r == 'POINTER':
        resultScope = 'pointer'
    if r == 'TEMP':
        resultScope = 'temp'
    
    result = f'\npush {resultScope} {n}'
    return result

def writePop(r, n):
    result=''
    resultScope = r
    if r == 'CONST':
        resultScope = 'constant'
    if r == 'ARG':
        resultScope = 'argument'
    if r == 'var':
        resultScope = 'local'
    if r == 'STATIC':
        resultScope = 'static'
    if r == 'THIS' or r =='field':
        resultScope = 'this'
    if r == 'THAT':
        resultScope = 'that'
    if r == 'POINTER':
        resultScope = 'pointer'
    if r == 'TEMP':
        resultScope = 'temp'
    
    result = f'\npop {resultScope} {n}'
    return result


def writeArithmetic(command):
    result=''
    result = f'\n{command}'
    return result

def writeArithmeticUsingOp(opText):
    result=''
    command = ''
    opList = ['+', '-', '*', '/', '&', '|', '<', '>', '=', '&lt;', '&gt;' , '&amp;']
    if opText == '+':
        command = 'add'
    elif opText == '-':
        command = 'sub'
    elif opText == '*':
        command = 'call Math.multiply 2'
    elif opText == '/':
        command = 'call Math.divide 2'
    elif opText == '&' or opText == '&amp;':
        command = 'and'
    elif opText == '|':
        command = 'or'
    elif opText == '<' or opText == '&lt;':
        command = 'lt'
    elif opText == '>' or opText == '&gt;':
        command = 'gt'
    elif opText == '=':
        command = 'eq'

    result = f'\n{command}'
    return result
    



def writeLabel(label):
    result=''
    result = f'\nlabel {label}'
    return result

def writeLabel(label):
    result=''
    result = f'\nlabel {label}'
    return result

def writeGoto(label):
    result=''
    result = f'\ngoto {label}'
    return result

def writeIf(label):
    result=''
    result = f'\nif-goto {label}'
    return result

def writeCall(name, n):
    result=''
    result = f'\ncall {name} {n}'
    return result

def writeFunction(name, n):
    result=''
    result = f'\nfunction {name} {n}'
    return result

def writeReturn():
    result=''
    result = f'\nreturn'
    return result

def templateIf(s1,s2,ifcnt):

    if s2 == '':
        result = f'''
    \nif-goto IF_TRUE{ifcnt}
goto IF_FALSE{ifcnt}
label IF_TRUE{ifcnt}
{s1}
label IF_FALSE{ifcnt}'''

    else:
        result = f'''
\nif-goto IF_TRUE{ifcnt}
goto IF_FALSE{ifcnt}
label IF_TRUE{ifcnt}
{s1}
goto IF_END{ifcnt}
label IF_FALSE{ifcnt}
{s2}
label IF_END{ifcnt}'''

    return result


def templateWhile(exp, s1, cnt):

    result = f'''
\nlabel WHILE_EXP{cnt}
{exp}
not
if-goto WHILE_END{cnt}
{s1}
goto WHILE_EXP{cnt}
label WHILE_END{cnt}'''