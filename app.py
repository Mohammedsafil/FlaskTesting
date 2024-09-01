### Building URL dynamically
### Variable Rules and URL Building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my App'

@app.route('/passed/<int:score>')
def passed(score):
    return f'You passed and Your score is {score}'

@app.route('/fail/<int:score>')
def fail(score):
    return f'You failed and Your score is {score}'

@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks<50:
        result = 'fail'
    else:
        result = 'passed'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)

