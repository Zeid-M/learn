from flask import Flask

app = Flask(__name__)


@app.route("/script")
def monitor():
    import subprocess

    p = subprocess.run("script.sh")
    return p.stdout


app.run(host="0.0.0.0", port=9876)
