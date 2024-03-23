from flask import Flask,render_template,request
import numpy as np
from model import map

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template("web.html")

@app.route("/result",methods=['POST','GET'])
@app.route("/result/",methods=['POST','GET'])
def result():
    outpt= request.form.to_dict()
    sc=int(outpt["School"])
    gy=int(outpt["Gym"])
    go=int(outpt["Gov"])
    sp=int(outpt["Shopping"])
    md=int(outpt["Medical"])
    st=int(outpt["Stat"])
    ex=int(outpt["Electronics"])
    gr=int(outpt["Grocery"])
    fd=int(outpt['Food'])
    hi=(sc,gy,go,sp,md,st,ex,gr)
    mp=map(sc,gy,go,sp,md,st,ex,gr,fd)
    mp.save("templates/trial.html")
    return render_template("web.html",mp=mp)

if __name__=='__main__':
    app.run(debug=True,port=5000)
 