
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        return render_template("1899.html",name=request.form.get("name"))
    else:
        return render_template("index.html")

