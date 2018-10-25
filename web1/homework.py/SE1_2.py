from flask import Flask, render_template
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def BMI(weight,height):
    b = weight
    a = height/100
    BMI = b/(a*a)
    if BMI < 16:
        return render_template("Severlyunderweight.html")
    elif 16 <= BMI < 18.5 :
        return render_template("Underweight.html")
    elif 18.5 <= BMI < 25 :
        return render_template("Normal.html")
    elif 25 <= BMI < 30 :
        return  render_template("Overweight.html")
    elif BMI > 30:
        return  render_template("Obese.html")

if __name__ == '__main__':
  app.run(debug=True)