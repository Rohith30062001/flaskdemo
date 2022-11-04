from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def helloworld():
    return "This is Flask app man"

@app.route('/login/<name>')
def login(name):
    return f"this is login page+{name}"

@app.route('/loginpage')
def loginpager():
    try:
        return "<h4><center>Welcome to login page</center></h4>"
    except:
        return "unable to load"


@app.route('/register')
def register():
    return render_template('register.html')

if __name__=='__main__':
    app.run(debug=True)

