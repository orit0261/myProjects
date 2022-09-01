from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content=["bill","joe"])

@app.route('/hello/<name>/')
def hello(name):
    """ Displays the page greats who ever comes to visit it.
    """
    return render_template('hello.html', name=name, r=2)

if __name__=="__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)