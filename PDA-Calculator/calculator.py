import copy
import math
from operator import add
from xml.etree.ElementTree import tostring

indexEntry = 0
mainList = list()
skop= list()
prefixChar = list()
sign = ""
size = 0
oper = ["+-" , "*/" , "^ exp ln sin cos tan sqrt abs ()", ]
def oper_func(s):
    z = -1
    for i in range(len(oper)):
        if s in oper[i]:
            return i
    return z 
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def is_operand(s):
    if s == "*":
        return True
    if s == "/":
        return True
    if s == "+":
        return True
    if s == "-":
        return True
    if s == "^":
        return True
    return False
def is_func(s):
    x = s.isalpha()
    return x
def is_par(s):
    if s == "(":
        return True
    if s == ")":
        return True
    else:
        return False
def what_is_the_Func(s):
    if (s == 'e'):
        s = 3
    elif (s == 'l'):
        s = 2
    elif (s == 'c'):
        s = 3
    elif (s == 't'):
        s = 3
    elif (s == 'a'):
        s = 3
    elif (s == 's'):
        s = 1
    elif (s == 'i'):
        s = 2
    elif (s == 'q'):
        s = 3
    return s
def add_to_list(s):
    global indexEntry
    if is_number(s[indexEntry]):
        global sign 
        cop = copy.deepcopy(indexEntry)
        while indexEntry < len(s) and is_number(s[indexEntry]):
            indexEntry += 1
        if indexEntry < size and s[indexEntry] == ".":
            indexEntry += 1
            while indexEntry < len(s) and is_number(s[indexEntry]):
                indexEntry += 1
        c = s[cop:indexEntry:1]
        if sign == "-":
            sl = sign + c
            sign = ""
            return sl
        return c
    elif is_operand(s[indexEntry]):
        if s[indexEntry] == '-':
            if indexEntry == 0:
                sign = "-"
                indexEntry += 1
                return
            if s[indexEntry - 1] == "(" or is_operand(s[indexEntry - 1]):
                sign = "-"
                indexEntry += 1
                return
        indexEntry += 1
        return s[indexEntry - 1]
    elif is_func(s[indexEntry]):
        cop = copy.deepcopy(indexEntry)
        x = what_is_the_Func(s[indexEntry])
        if x == 1:
            indexEntry += 1
            indexEntry += what_is_the_Func(s[indexEntry])
        else:
            indexEntry += what_is_the_Func(s[indexEntry])
        return s[cop: indexEntry : 1]
    elif is_par(s[indexEntry]):
        indexEntry += 1
        return s[indexEntry - 1]
def priority(s):
    z = 0
    for i in range(0 , len(oper)):
        if s in oper[i]:
            z = i
            return z
    return z
def add_to_stacks(li):
    for i in range(len(li)):
        if is_number(li[i]): 
            prefixChar.append(float(li[i]))
        elif is_operand(li[i]):
            if len(skop) == 0:
                skop.append(li[i])
            else:
                if priority(li[i]) >= priority(skop[len(skop) - 1]):
                    skop.append(li[i])
                else:
                    while len(skop)!= 0 and priority(skop[len(skop) - 1]) > priority(li[i]):
                        if skop[len(skop) - 1] == ")":
                            break
                        x = skop.pop(len(skop)-1)
                        prefixChar.append(x)
                    skop.append(li[i])
        elif is_func(li[i]):
            skop.append(li[i])
        elif is_par(li[i]):
            if li[i] == ")":
                skop.append(li[i])
            else:
                x = skop.pop(len(skop) - 1)
                if x == ")":
                    if i == 0:
                        return "INVALID"
                    if li[i - 1] == ")":
                        return "INVALID"
                while x != ")":
                    # prefixChar.append(x)
                    if len(skop) == 0:
                        return "INVALID"
                    else:
                        prefixChar.append(x)
                        x = skop.pop(len(skop) - 1)     
    while len(skop) != 0:
        y = skop.pop(len(skop) - 1)
        prefixChar.append(y)
    prefixChar.reverse()
    return prefixChar
def push_to_stack(li):
    result = list()
    while len(li) != 0:
        x = li.pop(len(li) - 1)
        if is_number(x):
            result.append(x)
        elif is_operand(x):
            if (len(result) < 2):
                return "INVALID"
            else:
                a = result.pop(len(result) - 1)
                b = result.pop(len(result) - 1)
                t = calculateOper(x, a, b)
                if t == "INVALID":
                    return t
                else:
                    result.append(t)
        elif is_func(x):
            if len(result) < 1:
                return "INVALID"
            else:
                a = result.pop(len(result) - 1)
                t = calculateFunc(x , a)
                if t == "INVALID":
                    return "INVALID"
                else:
                    result.append(t)
    if len(result) > 1:
        return "INVALID"
    else:
        a = result.pop(len(result) - 1)
        return f'{a:.2f}'
def calculateOper(oper, a , b):
    if oper == "^":
        return float(a)**float(b)
    if oper == "*":
        return float(a)*float(b)
    if oper == "/":
        if b == 0:
            return "INVALID"
        else:       
            return float(a)/float(b)
    if oper == "+":
        return float(a)+float(b)
    if oper == "-":
        return float(a)-float(b)
def calculateFunc(func , a):
    if func == "sqrt":
        if float(a) < 0:
            return "INVALID"
        else:
            return math.sqrt(a)
    elif func == "ln":
        if float(a) <= 0:
            return "INVALID"
        else:
            return math.log(float(a))
    elif func == "exp":    
        return math.e ** float(a)
    elif func == "sin":
        return math.sin(float(a))
    elif func == "cos":
        return math.cos(float(a))
    elif func == "tan":
        return math.tan(float(a))
    elif func == "abs":
        if float(a) > 0:
            return float(a)
        else:
            return float(a) * -1
def the_number_of_par(entry):
    if entry.count("(") != entry.count(")"):
        return False
    else:
        return True
entry = input().replace(" ", "")
size = len(entry)
if not the_number_of_par(entry):
    print("INVALID")
else:
    while(indexEntry != len(entry)):
        mainList.append(add_to_list(entry))
    mainList.reverse()
    while None in mainList:
        mainList.remove(None)
    res = copy.deepcopy(add_to_stacks(mainList))
    if res == "INVALID":
        print(res)
    else:
        a = push_to_stack(res)  
        print(a)