import copy
def adding_TO_list(mystr):
    main = list()
    mystr = mystr.replace(" ","")
    mylist = mystr.split("->")
    mylist1 = mylist[1].split("|")
    main.append(mylist[0])
    main += mylist1
    return main
def Func(inp, mylist, m):
    result = list()
    strr = "Rejected"
    result = copy.deepcopy(mylist[0])[1:]
    while len(result) != 0:
        jj = -1000
        res2 = list()
        for i in range(len(result)):
            for j in range(len(m)):
                if result[i].find(m[j]) != -1:
                    jj = j
                    break
            if jj == -1000:
                gg = acceptence(result[i],inp)
                if gg == 2:
                    strr = "Accepted"
                else:
                    result.remove(result[i])
                    res2 = copy.deepcopy(result)
                    break
            else:
                main = list()
                for h in range(1, len(mylist[jj])):
                    if mylist[jj][h] == "#":
                        s = result[i].replace(m[jj], "",1)
                    else:
                        s = result[i].replace(m[jj], mylist[jj][h],1)
                    gg = acceptence(s, inp)
                    if(gg == 0):
                        main.append(s)
                    if(gg == 2):
                        str = "Accepted"
                        return str
                    res2 = res2 + copy.deepcopy(main)#teghir
                    main.clear()
        result = copy.deepcopy(res2)       
    return strr
def hasLanda(mylist):
    z = 1
    for i in range(len(mylist)):
        if "#" in mylist[i]:
            z = 0
            break
    return z
def acceptence(a , b):
    xa = 0
    xb = 0
    z = 0
    if "<" not in a:
        if len(a) != len(b):
            z = 1
            return z
        else:
            for i in range(len(a)):
                if a[i] != b[i]:
                    z = 1
                    return z
            z = 2
            return z
    else:
        if (len(a) - destination(a)*3 > len(b) ):
            z = 1
            return z
        if (destination(a) > 1):
            if hasLanda(mainList) == 1:
                if destination(a) > len(b):
                    z = 1
                    return z
            if len(a) - destination(a) * 3 < len(b):
                if len(a) - destination(a) * 3 == 0:
                    z = 0
                    return z
                else:
                    if(a[-1] != ">"):
                        t = -1
                        ff = 0
                        while ff < len(a):
                            if a[ff] != "<":
                                if b.find(a[ff]) > t:
                                    if b.count(a[ff])< a.count(a[ff]):
                                        z = 1
                                        return z
                                    t = b.find(a[ff])
                                    ff += 1
                                else:
                                    z = 1
                                    return z
                            else:
                                ff += 3   
                        if t != len(b) - 1:
                            z = 1               
                        return z

                    else:
                        t = -1
                        ff = 0
                        while ff < len(a):
                            if a[ff] != "<":
                                if b.find(a[ff]) > t:
                                    if b.count(a[ff])!= a.count(a[ff]):
                                        z = 1
                                        return z
                                    t = b.find(a[ff])
                                    ff += 1
                                else:
                                    z = 1
                                    return z
                            else:
                                ff += 3                  
                        return z
        #     return z
        while(a[xa] != "<"):
            if(a[xa] != b[xb]):
                z = 1
                return z
            else:
                xa += 1
                xb += 1
        while(a[xa]!= ">"):
            xa += 1
        xa += 1
        i = 0
        j = 0
        while(i < len(a) - xa):
            if(a[len(a) - i - 1] != b[len(b) - j - 1]):
                z = 1
                return z
            else:
                j += 1
                i += 1
        return z

def destination(a): 
    res = a.count("<")
    return res

num = int(input())


mainList = list()
keysList = list()
for i in range(0 , num):
    mystr = input()
    mylist = adding_TO_list(mystr)
    mainList.append(mylist)
    keysList.append(mylist[0])
entry = input()
res = Func(entry, mainList, keysList)
print(res)


# 4
# <S> -> a<A> | a<B><B>
# <A> -> aa<A> | #
# <B> -> b<B> | bb<C>
# <C> -> <B>
# aaaaa
# aaa<A>
# aaabbbb     aa<A><B>bb     aa<A>a<B>bb