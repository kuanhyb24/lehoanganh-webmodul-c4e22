from flask import Flask, render_template
app = Flask(__name__)

@app.route("/BMI/<int:weight>/<int:height>")
def BMI(weight,height):
    b = weight
    a = height/100
    BMI = b/(a*a)
    if BMI < 16:
        return "Severely underweight"
    elif 16 <= BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Normal"
    elif 25 <= BMI < 30:
        return "Overweight"
    elif BMI > 30: 
        return "Obese"

if __name__ == '__main__':
  app.run(debug=True)