from flask import Flask, render_template, url_for, request
import smtplib
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sender", methods=["GET", "POST"])
def sender():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["mail"]
        sub = request.form["subject"]
        msg = request.form["message"]
        user = {"name": [name], "email": [email], "subject": [sub], "message": [msg]}
        print(user)
        my_email = 'sarikasethia2401@gmail.com'
        my_pass = "xwcjkjgkdsicnnau"
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(my_email, my_pass)
            connection.sendmail(from_addr=my_email, to_addrs=user["email"][0],
                                msg=f"Subject:{user["subject"][0]} \n\n {user["message"]}")
    return "email sent"

@app.route("/side",methods=['GET','POST'])
def side():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        user = {"name": name , "email":email,"subject":subject,"message":message}
        print(user)
        print(user["name"])
    return render_template("side.html")
if __name__ == "__main__":
    app.run(debug=True)
