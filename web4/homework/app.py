from flask import Flask, render_template
from river import River
import mlab
app = Flask(__name__)

mlab.connect()

# Ex2
@app.route("/river_africa")
def river_africa():
    river_list = River.object()
    for r in river_list:
        print(r.name)
    return render_template("Ex2.html", river = river_list)

# Ex3
@app.route("/river_america")
def river_america():
    short_river = River.object(length__lt=1000)
    for r in short_river:
        print(r.name)
    return render_template("Ex3.html", river = short_river)

if __name__ == '__main__':
  app.run(debug=True)