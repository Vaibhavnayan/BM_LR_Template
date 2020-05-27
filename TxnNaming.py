import os

def addStartContent(index,contents,newFilename):
    contents.insert(index, "web_reg_find(\"Text=textcheck\", \"SaveCount=WelcomeCount\", LAST); \n lr_start_transaction(\"Txn1\")\n")

    f = open(newFilename, "w")
    contents = "".join(contents)
    f.write(contents)
    
    index=index+2
    return index

def addEndContent(index2,contents,fileName):
    contents.insert(index2+1, "\n if(Textcheck){ \n lr_end_transaction(\"Txn1\",LR_PASS)\n} \n else { \n lr_end_transaction(\"Txn1\",LR_FAIL)\n}\n")
        
    f = open(fileName, "w")
    contents = "".join(contents)
    f.write(contents)
    
    index2=index2+2
    return index2


def openFileforStartTxn(index,fileName,newFilename):
    f = open(fileName, "r")
    contents = f.readlines()
    

    for items in contents:
        if ((len(contents)-1 >= index) and (contents[index].__contains__("web_"))): 
            index=addStartContent(index,contents,newFilename)
            print(index)          
            continue
        elif index==len(contents)-1:
            break
        else:
            index=index+1
    f.close()

def openFileforEndTxn(index2,fileName):
    f = open(fileName, "r")
    f.seek(0)
    contents = f.readlines()
    

    for items in contents:
        if ((len(contents)-1 >= index2) and (contents[index2].__contains__("LAST")) and not(contents[index2].__contains__("web_reg_find"))): 
            index2=addEndContent(index2,contents,fileName)
            print(index2, len(contents))          
            continue
        elif index2==len(contents)+1:
            break
        else:
            index2=index2+1
    f.close()

def mainFunc(oldfilePath,newfilePath):
    fileName = oldfilePath
    newFilename = newfilePath

    if(os.path.exists(fileName) and fileName.endswith(".c")):
        openFileforStartTxn(0,fileName,newFilename)
        openFileforEndTxn(0,newFilename)
        return "Done"
    else:
        return "File path doesn't exists"