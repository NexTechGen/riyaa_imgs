from flask import Flask, render_template
from img import get_list

app = Flask(__name__)

banner_name ="Riyaa Galaxy"
icon_img = "static/img_20190208_wa0005_gpW_icon.ico"

@app.route("/")
def hello_jovin():
  return render_template("home.html", 
                         paths = get_list(), 
                         name=banner_name, 
                          banner_imges = icon_img)  # home.html or home_bootstrap.html


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
