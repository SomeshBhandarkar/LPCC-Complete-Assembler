from instructionRecognizer import icConversion,assemblerDirectives
import re
import table as t
import os


def splitInputText(LC):
    file = open("input.txt", "r")
    file_content = file.read()
    list = file_content.split("\n")
    file.close()                        

    for i in list:
        delimiters = " ",",","+"
        regPat = '|'.join(map(re.escape, delimiters))
        splitted_list = re.split(regPat, i)
        LC = assemblerDirectives(splitted_list,LC)

def splitOutputText(LC):
    file = open("output.txt", "r")
    file_content = file.read()
    list = file_content.split("\n")
    file.close()  


    for i in list:
        delimiters = " "
        regPat = '|'.join(map(re.escape, delimiters))
        splitted_list = re.split(regPat, i)
        LC = icConversion(splitted_list)
        f = open("IC.txt", "a")
        f.write("\n")
        f.close() 

def main():
    if os.path.exists("output.txt"):
        os.remove("output.txt")

    if os.path.exists("IC.txt"):
        os.remove("IC.txt")
    LC = 0

    splitInputText(LC)
    splitOutputText(LC)     
    t.PrintTable()


if __name__ == '__main__':
    main()
    