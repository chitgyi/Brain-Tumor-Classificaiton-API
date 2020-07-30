from flask import Flask
from flask import request
from flask import jsonify, render_template
from Model import *

app = Flask(__name__, template_folder="public")


@app.route("/")
def hello():
    return render_template("index.html", title="App")


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]
    return jsonify(
        {
            "code": 200,
            "message": "Success",
            "data": {
                "score": Model.predict(),
                "type": "Leve 3",
                "image": image.filename,
                "imageType": image.content_type
            },
        }
    )


if __name__ == "__main__":
    app.run()
