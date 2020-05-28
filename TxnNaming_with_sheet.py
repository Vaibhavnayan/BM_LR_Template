import time #built-in libraries-  written inside pyton interpreter in C langauge- import sys sys.builtin_module_names
import os #standard libraries- written in both C in python, reside in python libraries. import sys sys.prefix
import pandas #third party libraries- written by third party- to install pip3 install pandas
import libraries

def addStartContent(index,contents,txnName,textCheck,value,newFilename):
    contents.pop(index)
    contents.insert(index, "web_reg_find(\"Text=%s\", \"SaveCount=TextCount\", LAST); \n lr_start_transaction(\"%s\");\n " %(textCheck[value],txnName[value]))
    
    f = open(newFilename, "w")
    contents = "".join(contents)
    f.write(contents)
    
    index=index+2
    return index

def addEndContent(index2,contents,txnName,textCheck,value,fileName):

    contents.insert(index2+1, "\n if(atoi(lr_eval_string(\"{%s}\")) > = 0){ \n lr_end_transaction(\"%s\",LR_PASS);\n} \n else { \n lr_end_transaction(\"%s\",LR_FAIL);\n}\n" %(textCheck[value],txnName[value],txnName[value]))
    contents.pop(index2)
        
    f = open(fileName, "w")
    contents = "".join(contents)
    f.write(contents)
    
    index2=index2+2
    return index2


def openFileforStartTxn(index,fileName,txnName,textCheck,newFilename):
    f = open(fileName, "r")
    contents = f.readlines()
    value=index

    for items in contents:
        if ((len(contents)-1 >= index) and (contents[index].__contains__("lr_start"))): 
            index=addStartContent(index,contents,txnName,textCheck,value,newFilename)
            value=value+1
            print(index)          
            continue
        elif index==len(contents)-1:
            break
        else:
            index=index+1
    f.close()

def openFileforEndTxn(index2,fileName,txnName,textCheck):
    f = open(fileName, "r")
    f.seek(0)
    contents = f.readlines()
    value=index2
    

    for items in contents:
        if ((len(contents)-1 >= index2) and (contents[index2].__contains__("lr_end"))): 
            index2=addEndContent(index2,contents,txnName,textCheck,value,fileName)
            value=value+1
            print(index2, len(contents))          
            continue
        elif index2==len(contents)+1:
            break
        else:
            index2=index2+1
    f.close()

def datasheet(sheetPath):
    if os.path.exists(sheetPath):
        content= pandas.read_csv(sheetPath)
        name=list(content.TxnName)
        textcheck=list(content.TextCheck)
        return (name,textcheck)
    else:
        return "File doesn't exist"

def mainFunc(oldfilePath,newfilePath,excelPath):
    fileName = oldfilePath
    newFilename = newfilePath
    sheetpath = excelPath
    if(os.path.exists(fileName) and fileName.endswith(".c") and newfilePath.endswith(".c")):
        lists= list(datasheet(sheetpath))
        txnName = list(lists[0])
        textCheck = list(lists[1])
        print(txnName[0])
        print(textCheck)
        openFileforStartTxn(0,fileName,txnName,textCheck,newFilename)
        openFileforEndTxn(0,newFilename,txnName,textCheck)
        return "Done"
    else:
        return "File path doesn't exists"