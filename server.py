from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    fruits = ['strawberry', 'raspberry', 'apple']
    fruitCounts = [int(request.form[fruits[0]]),int(request.form[fruits[1]]),int(request.form[fruits[2]])]
    fLen = len(fruits)
    for ind in range(fLen):
        fruits[ind] = fruits[ind].capitalize()
    sum = 0
    for f in fruitCounts:
        sum += f
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {sum} fruits")
    info = [request.form['first_name'], request.form['last_name'], request.form['student_id']]

    theTime = datetime.now().strftime("%b %d %Y %H:%M:%S")

    return render_template("checkout.html", fruits=fruits, fruitCounts=fruitCounts, info=info, totalItems=sum, fLen = fLen, theTime = theTime)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)