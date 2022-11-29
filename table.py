LTindex = 0        
PTindex = 0        
count = 0
STindex = 0
SymLC = 0
LitLC = 0

import lists as v

def STInsertion(temp_list,LC):
    temp1 = []
    global STindex
    temp1.append(STindex)
    STindex += 1
    temp1.append(temp_list[0])
    temp1.append(LC)
    v.symbolTable.append(temp1)
    LC += 1
    return LC

def LTInsertion(temp_list,LC):
    temp2 = []
    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            if(temp_list[i][j] == "="):
                global LTindex
                temp2.append(LTindex)
                temp2.append(temp_list[i][2])
                LTindex += 1
    v.literalTable.append(temp2)  
    return LC

def PTInsertion(LC):
    temp3 = []
    #global count
    count = -1
    for i in range(len(v.literalTable)):
        count += 1
    global PTindex
    temp3.append(PTindex)
    temp3.append(count)
    PTindex += 1
    v.poolTable.append(temp3)
    return LC

def LTAddLoc(LC):
    for i in range(len(v.literalTable)):
        if (len(v.literalTable[i]) < 3):
            v.literalTable[i].append(LC)
            LC += 1
    return LC

def UpdateLC(temp_list,LC):
    for i in range(len(temp_list)):
        for j in range(len(v.symbolTable)):    
            if (temp_list[i] == v.symbolTable[j][1]):
                LC = int(temp_list[2]) + v.symbolTable[j][2]
    return LC


def PrintTable():
    print("\nSymbol Table : ")
    print("\n".join(["  ".join(map(str, i)) for i in v.symbolTable]))
    print("\nLiteral Table : ")
    print("\n".join(["  ".join(map(str, i)) for i in v.literalTable]))
    print("\nPool Table : ")
    print("\n".join(["  ".join(map(str, i)) for i in v.poolTable]))
    

def checkinSYM(Ele):      
    for i in range(len(v.symbolTable)):
        if (Ele == v.symbolTable[i][1]):
            global SymLC
            v.temp.append(v.symbolTable[i][1])
            SymLC = v.symbolTable[i][0]
            return True
    return False
            

def checkinLT(Ele):
    for j in range(len(Ele)):
            if(Ele[j] == "="):
                for i in range(len(v.literalTable)):
                    if (Ele[j+2] == v.literalTable[i][1]):
                        global LitLC
                        LitLC = v.literalTable[i][0]
                        print(LitLC)
                        return True
    return False
        
    