from flask import Flask, request, render_template, send_file
from flask_restful import Resource, Api
import os
import personDetect

imgDirectory = os.path.join("static", "IMG")
app = Flask(__name__)
api = Api(app)

app.config["IMG_DIRECTORY"] = imgDirectory
imgPath = os.path.join(app.config["IMG_DIRECTORY"], "img.jpg")

@app.route('/', methods=['GET'])
def test():
    a = "hej"
    return a

@app.route("/img", methods=["POST"])
def FindPeople():
    if request.method == 'POST':
        if "img" in request.files and request.files["img"].filename != "":
            image = request.files["img"]
            image.save(imgPath)
            personDetect.personDetectionFromImage(image.filename)
            b = "dziala"
            return b
            #return render_template("img.html", user_image=imgPath)
        else:
            a = "hej"
            return a


if __name__ == '__main__':
    app.run(debug=True)
