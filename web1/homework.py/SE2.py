from flask import Flask, render_template
app = Flask(__name__)

@app.route("/user/<username>")
def user_name(username):
        user = {
                'huy' : {
                'name' : 'Nguyen Quang Huy',
                'age' : 29
                },
                'tuananh' : {
                'name' : 'Huynh Tuan Anh',
                'age' : 22
                        },
                }
        if username in user.keys():
                return render_template("optinal.html", user = user[username])
        else:
                return "User not found"

if __name__ == '__main__':
  app.run(debug=True)