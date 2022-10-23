from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods =["POST"])
def login():
    if request.method == "POST" :
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_phone = request.form["phone"]
        return render_template('index.html',name = user_name, email = user_email, phone = user_phone)

if __name__ == ('__main__'):
    app.run(debug = True)
