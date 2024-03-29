from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")             #endpoint
@app.route("/home")
def home():
    return render_template("home.html") #looking for project/templates/home.html

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)