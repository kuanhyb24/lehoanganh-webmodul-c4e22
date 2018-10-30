from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/new_bike", methods=['GET', 'POST'])
def new_bike():
    if request.method == 'GET':
        return render_template("Bike_Rental_Service.html")
    elif request.method == 'POST':
        form = request.form
        model = form['model']
        fee = form['fee']
        image = form['image']
        year = form['year']
        print(model,fee,image,year)
        return 'Submit Thành Công'
if __name__ == '__main__':
  app.run(debug=True)

