from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=["POST"])
def get_name():
    print("Hello, World!")
    return "<p>Hello World!</p>"


if __name__ == "__main__":
    app.run(debug=True)