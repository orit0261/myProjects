from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.secret_key= "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email = email


# or, without the decorator
@app.route("/")
def home():
    flash("You have been logout","info")

    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
    flash("You have been login","info")

    if request.method=="POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_usr = users.query.filter_by(name=user).first()
        if found_usr:
            session["email"] = found_usr.email
        else:
            usr = users(user,"")
            db.session.add(usr)
            db.session.commit()

        flash("Login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Login!")
            return redirect(url_for("user"))

    return render_template("login.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/logout")
def logout():
    flash("You have been logout","info")
    session.pop("user",None)
    session.pop("email",None)

    return redirect(url_for("login"))

@app.route("/user",methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method=='POST':
            email = request.form["email"]
            session["email"]=email
            flash("Email was saved!")
            found_user = users.query.filter_by(name=user).first()
            #found_user = users.query.filter_by(name=user).delete() delete one user
            # del all users
            # for usr in foound_user:
               #usr.delete() delete  user
            # db.session.commit()


            found_user.email = email
            db.session.commit()
            flash("Email saved")
        else:
            if "email" in session:
               email  = session["email"]

        return render_template("product.html",email=email)
    else:
        flash("you are not logged in!")

@app.route("/view")
def view():
    return render_template("view.html",values=users.query.all())

if __name__=="__main__":
    db.create_all() # create the db if it doesnt exists
    app.run(debug=True)