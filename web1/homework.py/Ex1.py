import os
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/about-me/")
def me():
  return render_template("about-me.html")

@app.route("/school")
def teckids():
  return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)