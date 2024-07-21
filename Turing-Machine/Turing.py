def languageOfTuringMachine(s):
    arr = s.split('00')
    size = len(arr)
    mylist = list()
    for j in range(size):
        mylist.append(arr[j].split('0'))
    return mylist
def final_state(mylist):
    max = ''
    for u in range(len(mylist)):
        if(len(mylist[u][0]) > len(max)):
            max = mylist[u][0]
        if(len(mylist[u][2]) > len(max)):
            max = mylist[u][2]
    return max
def find_state_index(mylist, s, start_state):
    z = -1000
    for k in range(len(mylist)):
        if(mylist[k][1] == s and mylist[k][0] == start_state):
            z = k
            break
    return z
def travelOnTape(mylist, navar):
    if(len(navar) == 0):
        navar = '1'
    result_string = "Rejected"
    index = 30
    gg = final_state(mylist)
    blank = ['1','1','1','1','1','1','1','1','1','1',
             '1','1','1','1','1','1','1','1','1','1',
             '1','1','1','1','1','1','1','1','1','1'] 
    start_state = '1'
    tape = blank + navar.split('0') + blank 
    while(True):
        res = find_state_index(mylist, tape[index], start_state)
        if res == -1000:
            if start_state == gg:
                result_string == "Accepted"
            break
        else:
            start_state = mylist[res][2]
            tape[index] = mylist[res][3]
            if(mylist[res][4] == '1'):
                index -= 1
            else:
                index += 1
    if start_state == gg:
        result_string = "Accepted"
    return result_string
s = input()
num = int(input())
for i in range(0, num):
    zaban = input()
    print(travelOnTape(languageOfTuringMachine(s), zaban))