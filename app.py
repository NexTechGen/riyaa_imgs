from flask import Flask, render_template
from img import get_list

app = Flask(__name__)


@app.route("/")
def hello_jovin():
  return render_template("home.html")  # home.html or home_bootstrap.html


print(get_list())

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
