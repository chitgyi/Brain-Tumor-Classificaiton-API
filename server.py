from flask import Flask
from flask import request
from flask import jsonify, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import utils as funs



app = Flask(__name__, template_folder="public")
model = load_model("./brain-tumor-model.h5")


@app.route("/")
def hello():
    return render_template("index.html", title="App")


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]
    image.save("images/" + image.filename)
    loadedImage = Image.open("images/" + image.filename).convert('LA')
    x = np.array(loadedImage.resize((150, 150)))
    x = x.reshape(-1, 150, 150, 2)
    answ = model.predict_on_batch(x)
    classification = np.where(answ == np.amax(answ))[1][0]
    return jsonify(
        {
            "code": 200,
            "message": "Success",
            "data": {
                "type": funs.names(classification),
                "score": answ[0][classification]*100,
                "image": image.filename,
                "imageType": image.content_type,
            },
        }
    )


if __name__ == "__main__":
    app.run()
