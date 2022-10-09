import smtplib
import csv
import re
from flask import Flask,request,render_template,flash
email_condition=r"^[a-z]+[\._]?[A-Z 0-9]+[@]\w+[.]\w{2,3}$"
app=Flask(__name__)
pure=[]
unpure=[]
# email="kvand321@gmail.com"
# password='lpulieeoheqkeond'
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/uploaded',methods=['GET','POST'])
def data():
     return render_template('uploaded.html')

@app.route('/purify1')
def second():
    return render_template("purify.html")
@app.route('/invalid')
def third():
    return render_template("ulist.html",clist=unpure)

@app.route('/send',methods=['GET','POST'])
def fourth():
     return render_template('send.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if(request.method=='POST'):
        email=request.form['email']
        password=request.form['password']
        subject=request.form['subject']
        body=request.form['compose']
        f=request.files['file1']
        name=f.filename
        
    data=[]
    data1=[]
    pur=[]
    puri=[]
    # unp=[]
    with open(name,'r',encoding="utf-8") as file:
        csvf=csv.reader(file)
        for row in csvf:
            print(row)
            data.append(row)
            data1=data[1:]
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.set_debuglevel(1)
        smtp.login(email,password)
        # subject="hi"
        # body="hello"
        msg=f'subject:{subject}\n\n{body}'
        for mails in data1:
            # if re.search(email_condition,'mails[0]'):
            pur.append(mails[0])
            
               
        for items in pur:
            # print(items)
            # for i in range(len(pur)):
            if re.search(email_condition,items):
                puri.append(items)
                # else:
                    # unp.append(item)
                smtp.sendmail(email,items,msg)
                # print('sent to',mails)
        # smtp.sendmail(email,puri,msg)

        smtp.close()
    return render_template("index.html",success=True)
@app.route('/purify',methods=['GET','POST'])
def purify():
    if(request.method=='POST'):
        f=request.files['file1']
        name=f.filename
    datas=[]
    data2=[]
    # pure=[]
    # unpure=[]
    alls=[]
    # unp=[]
    with open(name,'r',encoding="utf-8") as file:
        csvf=csv.reader(file)
        for row in csvf:
            print(row)
            datas.append(row)
            data2=datas[1:]
        for mails in data2:
            alls.append(mails[0])   
        for mails in alls:
            if re.search(email_condition,mails):
                pure.append(mails)
            else:
                unpure.append(mails)
    return render_template("listp.html",plist=pure,ulist=unpure)


if __name__=='__main__':
    app.run(debug=True)
