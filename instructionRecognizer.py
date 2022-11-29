import table as t
import emotAndIcType as e
Class = 0
Opcode = 0

def CheckEMOT(Instr):
    for i in range(len(e.EMOTable)):
        if (Instr == e.EMOTable[i][0]):
            global Class,Opcode
            Class = e.EMOTable[i][1]
            Opcode = e.EMOTable[i][2]
            return True
    return False

def checkInstanceType(Instr):
    result = []
    for i in range(len(e.InstructionType)):
        if (Class == e.InstructionType[i][0]):
            result.append(e.InstructionType[i][1])
            result.append(Opcode)
            Str1 = ','.join(map(str,result))
            return Str1
        

def output(LC,temp_list):
    Str1 = ' '.join(map(str,temp_list))
    f = open("output.txt", "a")
    f.write(str(LC) + " " + Str1 + '\n')
    f.close()
    

def assemblerDirectives(temp_list,LC):
    if ( temp_list[0] == 'START' ):
        LC = int(temp_list[1])
        output(LC,temp_list)
        LC

    elif ( temp_list[0] == 'READ' ):
        output(LC,temp_list)
        LC += 1

    elif ( temp_list[0] == 'MOVER' ):
        output(LC,temp_list)
        LC += 1

    elif ( temp_list[0] == 'MOVEM' ):
        output(LC,temp_list)
        LC += 1
        
    elif ( temp_list[0] == 'ADD' ):
        output(LC,temp_list)
        LC += 1

    elif ( temp_list[0] == 'MULT' ):
        output(LC,temp_list)
        LC += 1
    
    elif ( temp_list[0] == 'SUB' ):
        output(LC,temp_list)
        LC += 1
    
    elif ( temp_list[0] == 'COMP'):
        output(LC,temp_list)
        LC += 1
    
    elif ( temp_list[0] == 'PRINT'):
        output(LC,temp_list)
        LC += 1
        
    elif ( len(temp_list) == 4 ):
        output(LC,temp_list)
        LC = t.STInsertion(temp_list,LC)
        
    elif ( temp_list[0] == "LTORG"):
        output(LC,temp_list)
        LC = t.LTAddLoc(LC)
        LC = t.PTInsertion(LC)
        
    elif ( temp_list[0] == "STOP"):
        output(LC,temp_list)
        LC += 1
    
    elif ( temp_list[0] == "END"):
        output(LC,temp_list)
        LC = t.LTAddLoc(LC)
    
    elif ( temp_list[1] == "EQU"):
        output(LC,temp_list)
        LC = t.STInsertion(temp_list,LC)
        
    elif ( temp_list[0] == "BC"):
        output(LC,temp_list)
        LC += 1
    
    elif ( temp_list[0] == "ORIGIN"):
        output(LC,temp_list)
        LC = t.UpdateLC(temp_list,LC)
        
    else:
        for k  in range(len(temp_list)):
            if (temp_list[k] == "DS"):
                output(LC,temp_list)
                LC = t.STInsertion(temp_list,LC) + (int(temp_list[2]) - 1)
                
    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            if(temp_list[i][j] == "="):
                LC = t.LTInsertion(temp_list,LC)

    return LC


def icConversion(temp_list):
    f = open("IC.txt", "a")

    for i in range(len(temp_list)):
        if (CheckEMOT(temp_list[i])):
            IClist = checkInstanceType(temp_list[i])
            f.write("(" + str(IClist) + ")")

        elif (t.checkinSYM(temp_list[i])): 
            f.write("(" + "S" + "," + str(t.SymLC) + ")")

        elif (t.checkinLT(temp_list[i])):
            if (i != 0):
                f.write("(" + "L" + "," + str(t.LitLC) + ")")

        else:
            if(i == 0):
                f.write(str(temp_list[i]) + " ")
            else:
                f.write("(" + "C" + "," + str(temp_list[i]) + ")")
                
    f.close()