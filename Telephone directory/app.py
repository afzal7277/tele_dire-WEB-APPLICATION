from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
td={}
@app.route("/add",methods=["GET","POST"])
def add():
    fname=request.form.get("fname")
    number=request.form.get("number")
    if (fname==None and number==None) or (fname=="") or (number=="") :
        pass
    else:
        td[fname]=number
    return render_template("add.html",td=td)
@app.route("/display")
def display():

    return render_template("display.html",td=td)
@app.route("/search")
def search():

    return render_template("search.html",td=td)
if __name__=="__main__":
    app.run(debug=True)
