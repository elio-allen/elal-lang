import sys

ptr = 0

checklist = {}

fileElal = sys.argv[1]

f = open(fileElal, "rb")

bFileElal = f.read()
#print(bFileElal)
hFileElal = []
for i in bFileElal :
    hFileElal.append(hex(i).split('x')[-1])

#print(hFileElal)
if(hFileElal[0] != "31" or hFileElal[1] != "a1"):
    
    raise Exception("Fix your header!")

ptr = 3
h = hFileElal

def getVar(varname):
    temp_old = h.index(varname)
    temp = h.index(varname, temp_old + 1)
    varValue = []

    while h[temp] != "0" and h[temp] != "1":
        varValue.append(h[temp])
        temp = temp + 1
    del varValue[0]
#    print(varValue)
    crlf = True
    if h[temp] == "1":
        crlf = False

    return varValue, temp, crlf

def getPrint(varname,where):
    temp = h.index(varname, where)
#    print(temp)
    varValue = []

    while h[temp] != "0" and h[temp] != "1":
        varValue.append(h[temp])
        temp = temp + 1
    crlf = True
    if h[temp] == "1":
        crlf = False

    return varValue, temp, crlf

while ptr != len(hFileElal):

    if h[ptr] == "11":

        while h[ptr] == "11":
            if h[ptr + 2] == "fd":

                if h[ptr + 1] not in checklist:
                    
                    varValue, lengthVar, crlf = getVar(h[ptr + 1])
                    asciiVarValue = ""
                    for i in varValue:
                        asciiVarValue = asciiVarValue + bytes.fromhex(i).decode('ascii')
                    checklist.update({f"{h[ptr+1]}":f"{asciiVarValue}"})
###                   this was breaking my code, don't uncomment
##                    print(checklist)
##                    print(asciiVarValue, "herr")
##                    ptr = ptr + lengthVar - 2
                else:
                    #print(checklist[h[ptr + 1]])
                    varValue, lengthVar, crlf = getVar(h[ptr + 1])
                    if crlf:
                        print(checklist[h[ptr + 1]])
                    else:
                        print(checklist[h[ptr + 1]], end="")
                    ptr = ptr + 4

            else:

                varValue, lengthVar, crlf = getPrint(h[ptr + 1], ptr)
                asciiVarValue = ""
                for i in varValue:
                    asciiVarValue = asciiVarValue + bytes.fromhex(i).decode('ascii')
                checklist.update({f"{h[ptr+1]}":f"{asciiVarValue}"})
                #print(crlf)
                if crlf:
                    print(asciiVarValue)
                else:
                    print(asciiVarValue, end="")
                ptr = lengthVar - 2 # minus two for end and start (example: e0 and 01)


    if h[ptr] == "12":
        getCurrVar = h[ptr + 1]
        asciiVarValue = input()
        checklist.update({f"{h[ptr+1]}":f"{asciiVarValue}"})
        ptr = ptr + 3

    if h[ptr] == "ff":
        break
    if h[ptr] != "ff" and h[ptr] != "12" and h[ptr] != "11" :
        # keep it moving in case my code broke
        ptr = ptr + 1

    
