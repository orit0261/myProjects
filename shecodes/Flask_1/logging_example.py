from flask import Flask, redirect, url_for, logging, request
import logging
from logging.handlers import SMTPHandler

logging.basicConfig(filename='demo.log',level=logging.DEBUG)

mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['orit0261@google.com'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

app = Flask(__name__)
if not app.debug:
    app.logger.addHandler(mail_handler)


@app.route("/")
def home():
    app.logger.info('Processing default request')
    return "Hello! this is the main page <h1>HELLO<h1>"

# take name as param, type /orit or /home as name param
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)

