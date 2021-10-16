# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_method():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    
    return str(result)

@app.route("/sub")
def sub_method():
    """Substitue a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    
    return str(result)

@app.route("/mult")
def mult_method():
    """Multiply a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    
    return str(result)

@app.route("/div")
def div_method():
    """Division a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    
    return str(result)

# Further Study
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}
@app.route("/math/<operator>")
def math(operator):
    """Do math with a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a,b)

    return str(result)



