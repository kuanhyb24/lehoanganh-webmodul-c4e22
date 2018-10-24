from flask import Flask, render_template

app = Flask(__name__) #cho thu vien biet flask nam o vi tri nao

@app.route("/") # neu nhu nguoi dung truy cap vao trang chu thi goi ham ben duoi
def homepage():
    return("welcome to c4e web modul, enjoy,")

@app.route("/hoanganh")
def hello_hoanganh():
    return "Hello Hoang Anh"

@app.route("/praise/Quan")
def praise_Quan():
    return "Quan is awsome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awsome"

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    s = x + y
    return str(s)
  
@app.route("/question")
def show_question():
    return render_template("question.html")
   
    

if __name__ == "__main__":
    app.run(debug=True) #reset lai server