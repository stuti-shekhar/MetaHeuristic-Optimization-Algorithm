from flask import request, render_template, Flask, url_for, redirect
from predict import fitness, fitness1, fitness2

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/predict',methods=["GET","POST"])
def predict():
    if(request.method=="POST"):
        d = dict()
        req = request.form
        d['absences'] = req["absences"]
        d['activities'] = req["activities"]
        d['age'] = req["age"]
        d['Dalc'] = req["dalc"]
        d['failures'] = req["failures"]
        d['famrel'] = req["famrel"]
        d['Fedu'] = req["fedu"]
        d['Fjob'] = req["fjob"]
        d['freetime'] = req["freetime"]
        d['G1'] = req["G1"]
        d['G2'] = req["G2"]
        d['goout'] = req["goout"]
        d['guardian'] = req["gaurdian"]
        d['health'] = req["health"]
        d['Medu'] = req["medu"]
        d['nursery'] = req["nursery"]
        d['paid'] = req["paid"]
        d['reason'] = req["reason"]
        d['romantic'] = req["romantic"]
        res = (fitness(0, d))
        G1 = int(d["G1"])
        G2 = int(d["G2"])
        print(res)
        if G1<=5:
            G1 = 1
        elif G1>5 and G1<11:
            G1 = 2
        elif G1>=11 and G1<16:
            G1 = 3
        else:
            G1 = 4
        if G2<=5:
            G2 = 1
        elif G2>5 and G2<11:
            G2 = 2
        elif G2>=11 and G2<16:
            G2 = 3
        else:
            G2 = 4
        if res == 0:
            min = 0
            max = 5
        if res == 1:
            min = 6
            max = 10
        if res == 2:
            min = 11
            max = 15
        if res == 3:
            min = 16
            max = 20
        print(1, min,max)
        res1 = (fitness1(0, d))
        if res1 == 0:
            min1 = 0
            max1 = 5
        if res1 == 1:
            min1 = 6
            max1 = 10
        if res1 == 2:
            min1 = 11
            max1 = 15
        if res1 == 3:
            min1 = 16
            max1 = 20
        res2 = (fitness2(0, d))
        if res2 == 0:
            min2 = 0
            max2 = 5
        if res2 == 1:
            min2 = 6
            max2 = 10
        if res2 == 2:
            min2 = 11
            max2 = 15
        if res2 == 3:
            min2 = 16
            max2 = 20
        return redirect(url_for("results",res = res +1 ,min = min, max = max,min1 = min1, max1 = max1,min2 = min2, max2 = max2,G1= G1,G2= G2))
    return render_template("form1.html")

@app.route('/results',methods=["GET","POST"])
def results():
    min  = request.args.get("min")
    max  = request.args.get("max")
    min1 = request.args.get("min1")
    max1 = request.args.get("max1")
    min2 = request.args.get("min2")
    max2 = request.args.get("max2")
    G1 = request.args.get("G1")
    G2 = request.args.get("G2")
    G3 = request.args.get("res")
    print(2,min,max)
    return render_template("generic.html", min = min, max = max,min1 = min1, max1 = max1,min2 = min2, max2 = max2,G1 = G1, G2 = G2, G3 = G3)
if __name__ == '__main__':
    app.run(debug=True)