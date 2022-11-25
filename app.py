from flask  import Flask, render_template,request,redirect,url_for


app=Flask(__name__)
@app.route("/")
def index():
    numbers=[1,2,3,4,5,6,7]

    return render_template("index.html",numbers=numbers)
"""@app.route("/search")
def search():
    return "search page"
@app.route("/delete/item")
def  delete():
    return "delete item" 
@app.route("/delete/<string:id>")
def deleteId(id):
    return "Id: " + id"""


@app.route("/toplam", methods=["GET","POST"])
def toplam():
   if request.method=="POST":
    
    number1=request.form.get("number1")
    number2=request.form.get("number2") 
    return render_template("number.html",total=int(number1)+int(number2) ) 
   else:
    #return render_template("number.html")
    return redirect (url_for("index"))
if __name__=="__main__":
    app.run(debug=True)

app.run()