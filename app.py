from flask import Flask, app, render_template, request

app = Flask(__name__)  # instance of flask running

@app.route('/')
def index():
    # title = "Main Page" # its not the convention to pass view data from here as this is just a controller page
    return render_template("index.html")

@app.route('/about')
def about():
    names = ["Anuj","Owais","Naveen"]  # its not the convention to pass view data from here as this is just a controller page
    list1 = [1,2,3,4,5]
    list2 = ["one","two","three","four","five"]
    list3 = zip(list1,list2)
    return render_template("about.html", names=names, list3=list3)

@app.route('/sub')
def sub():
    return render_template("sub.html")

@app.route('/form', methods=["POST"])
def form():
    name = request.form.get("name")
    password = request.form.get("password")
    if not name:
        error = "name is missing" 
        return render_template("sub.html", password=password, error=error)
    elif not password:
        error = "password is missing"
        return render_template("sub.html", name=name, error=error)
    return render_template("form.html", name=name , password=password)


