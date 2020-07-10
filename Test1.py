from flask import Flask, render_template, request,jsonify, redirect, Response, make_response,send_file
import TxnNaming
import TxnNaming_with_sheet
import TxnNaming_API
import os

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/success2')
def success2():
    return render_template('success2.html')

@app.route('/error2')
def error2():
    return render_template('error2.html')

@app.route('/LR_Template')
def LR_Template():
    return render_template('index.html')

@app.route('/LR_Template_With_Excel')
def LR_Template_With_Excel():
    return render_template('index2.html')    
    
@app.route('/conversionDone', methods = ['POST'])
def conversionDone():
    filePath = request.form['filePath']
    newfilePath = request.form['newfilePath']
    response1 = TxnNaming.mainFunc(filePath,newfilePath)
    #print("The file path is '" + filePath + "'" + newfilePath+ " " + response1)
    if response1 == "File doesn't exists":
        return redirect('/error')
    elif not(newfilePath.endswith(".c")):
        return redirect('/error')
    else:
        return redirect('/success')

@app.route('/conversionDone2', methods = ['POST'])
def conversionDone2():
    #filePath = request.form['filePath']
    
    #excelPath = request.form['excelPath']
    script_type = request.form['scripts']
    filePath = request.files['filePath']
    newfilePath = filePath.filename
    excelPath = request.files['excelPath']

    if (script_type == "WEB"):
        response1, fileName, data = TxnNaming_with_sheet.mainFunc(filePath,newfilePath,excelPath)
        #print("The file path is '" + response1 +""+fileName+""+data)
        if response1 == "File path doesn't exists":
            return redirect('/error2')
        elif not(newfilePath.endswith(".c")):
            return redirect('/error2')
        else:
            return Response(data,
                             mimetype="text/c",
                             headers={"Content-disposition":
                                     "attachment; filename={}".format(fileName)})
            #return redirect('/success2')

    elif (script_type == "API"):
        response1, fileName, data = TxnNaming_API.mainFunc(filePath,newfilePath,excelPath)
        #print("The file path is '" + filePath + "'" + newfilePath+ " " + response1 + "" + excelPath +" " + script_type)
        if response1 == "File path doesn't exists":
            return redirect('/error2')
        elif not(newfilePath.endswith(".c")):
            return redirect('/error2')
        else:
            return Response(data,
                         mimetype="text/c",
                         headers={"Content-disposition":
                                 "attachment; filename={}".format(fileName)})
            

if __name__== "__main__":
    app.run(debug=True)
