from flask import Flask, render_template, request, redirect
import TxnNaming
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
    return render_template('Error.html')

@app.route('/LR_Template')
def LR_Template():
    return render_template('index.html')
    
@app.route('/conversionDone', methods = ['POST'])
def conversionDone():
    filePath = request.form['filePath']
    newfilePath = request.form['newfilePath']
    response1 = TxnNaming.mainFunc(filePath,newfilePath)
    print("The file path is '" + filePath + "'" + newfilePath+ " " + response1)
    if response1 == "File doesn't exists":
        return redirect('/error')
    elif not(newfilePath.endswith(".c")):
        return redirect('/error')
    else:
        return redirect('/success')
if __name__== "__main__":
    app.run(debug=True)
