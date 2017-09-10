from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count=0
app.random=0
app.str=""
@app.route("/")
def index():
    print app.count
    return render_template("index.html",gold=app.count,random=app.random,str=app.str)
@app.route("/process",methods=["POST","GET"])
def gold(): 
    import random
    if request.method == "POST":
        
        if "farm" in request.form:
            app.random = random.randrange(10,20)
            app.count += app.random
            
            app.str = "You have earned", app.random
            print app.random
            print app.str
            # return redirect("/")

        elif "acave" in request.form:
            app.random = random.randrange(5,10)
            app.count += app.random
            
            app.str = "You have earned", app.random
            print app.random
            print app.str
            # return redirect("/")

        elif "house" in request.form:
            app.random= random.randrange(1,5)
            app.count += app.random
            
            app.str = "You have earned", app.random
            print app.random
            print app.str
            # return redirect("/")

        elif "casino" in request.form:
            if random.randint(0,100) >= 40:
                app.random = 50
                app.count += app.random
                app.str = "You have earned", app.random
            else:
                app.random = 50
                app.count -= app.random
            
            app.str = "You have lost", app.random
            print app.random
            print app.str
            # return redirect("/")
    return redirect("/")
    
@app.route("/clear", methods=["POST"])
def clear():
    app.count = 0
    return redirect("/")
app.run(debug=True)