import werkzeug
from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

# or, without the decorator
app.register_error_handler(400, handle_bad_request)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
       return render_template("login.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__=="__main__":
    app.run(debug=True)