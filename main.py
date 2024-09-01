### How to Integrate to HTML and Flask


from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/checker/<int:score>')
def checker(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"
    dir = {'score' : score, 'result':res}
    return render_template('result.html',result=dir)


@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks<50:
        result = 'fail'
    else:
        result = 'passed'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science = float(request.form.get('science'))
        maths  = float(request.form.get('maths'))
        c = float(request.form.get('c'))
        ds = float(request.form.get('datascience'))
        total_score = (science+maths+c+ds)/4
    return redirect(url_for('checker',score=total_score))

if __name__=='__main__':
    app.run(debug=True)

