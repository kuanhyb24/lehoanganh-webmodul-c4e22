from flask import Flask, render_template, request
from reg import Reg
import mlab
from random import choice

app = Flask(__name__)
mlab.connect()

@app.route("/")
def home():
    return "Xin Chào!"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        form = request.form
        firstname = form['firstname']
        lastname = form['lastname']
        email = form['email']
        yob = form['yob']
        gender = form['gender']
        print(firstname,lastname,email,yob,gender)
        alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        code = ""
        for _ in range(6):
            code += choice(alphabet)
        r = Reg(firstname=firstname, lastname=lastname, email=email, yob=yob, gender=gender, code=code)
        r.save()
        return "Hoàn Thành"
if __name__ == '__main__':
  app.run(debug=True)