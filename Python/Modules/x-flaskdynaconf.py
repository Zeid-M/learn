from dynaconf import FlaskDynaconf

from flask import Flask

app = Flask(__name__)
FlaskDynaconf(app, settings_files=["settings.toml"])


@app.route("/a_view")
def a_view():
    return "hi"


# print(app.config.name)

app.run(host=app.config.HOST, port=app.config.PORT)
