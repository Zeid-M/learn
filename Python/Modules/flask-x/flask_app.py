from werkzeug import secure_filename

from flask import Flask, redirect, render_template, request, url_for

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
#  which URL is associated function
@app.route("/")
def hi():
    return "hi"


# decorator to route URL
@app.route("/bye")
def bye():
    return "bye"


@app.route("/hello")
def hello_world():
    return "hello world"


## Variables in Flask
#  routing the decorator function hello_name
@app.route("/hello/<name>/<age>")
def hello_name(name, age):
    return f"hello {name} {age}"


@app.route("/admin")  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return "Hello Admin"


@app.route("/guest/<guest>")
def hello_guest(guest):  # binding to hello_guest call
    return "Hello %s as Guest" % guest


@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":  # dynamic binding of URL to function
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))


@app.route("/upload")
def upload_file():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))


if __name__ == "__main__":

    # app.run()

    # debug mode to update the changes in the code
    app.run(debug=True)
