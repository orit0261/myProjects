from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.secret_key= "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///products.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

class products(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    pr_name = db.Column(db.String(100))


    def __init__(self,pr_name):
        self.pr_name = pr_name


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
        product = request.form["nm"]
        session["product"] = product

        found_prod = products.query.filter_by(pr_name=product).first()
        if found_prod:
            session["pr_name"] = found_prod.pr_name
        else:
            prod = products(product)
            db.session.add(prod)
            db.session.commit()

        flash("Login successful!")
        return redirect(url_for("product"))
    else:
        if "product" in session:
            flash("Already Login!")
            return redirect(url_for("product"))

    return render_template("login.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/logout")
def logout():
    flash("You have been logout","info")
    session.pop("product",None)
    session.pop("pr_name",None)

    return redirect(url_for("login"))

@app.route("/product",methods=["POST","GET"])
def product():
    pr_name = None
    if "product" in session:
        product = session["pr_name"]
        if request.method=='POST':
            pr_name = request.form["pr_name"]
            session["pr_name"]=pr_name
            flash("Email was saved!")
            found_user = products.query.filter_by(pr_name=product).first()
            #found_user = products.query.filter_by(pr_name=product).delete() delete one product
            # del all products
            # for prod in foound_user:
               #prod.delete() delete  product
            # db.session.commit()


            found_user.pr_name = pr_name
            db.session.add(found_user)
            db.session.commit()
            flash("Email saved")
        else:
            if "pr_name" in session:
               pr_name  = session["pr_name"]

        return render_template("product.html",pr_name=pr_name)
    else:
        flash("you are not logged in!")

@app.route("/view")
def view():
    return render_template("view.html",values=products.query.all())

if __name__=="__main__":
    db.create_all() # create the db if it doesnt exists
    app.run(debug=True)