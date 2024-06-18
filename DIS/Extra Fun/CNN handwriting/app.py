import numpy as np
import tensorflow as tf
import cv2
import base64
from flask import Flask, request, jsonify, render_template

# Load the trained model
model = tf.keras.models.load_model("mnist_cnn.h5")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the image data from the request
        data = request.json["image"]
        # Decode the base64 image
        img_data = base64.b64decode(data.split(",")[1])
        with open("image.png", "wb") as f:
            f.write(img_data)

        # Preprocess the image
        img = preprocess_image("image.png")
        if img is None:
            return jsonify({"error": "Invalid image data"})

        # Predict the digit
        digit = predict_digit(img)

        return jsonify({"digit": int(digit)})

    except Exception as e:
        return jsonify({"error": str(e)})


def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        return None

    # Ensure the image has a white background
    if img.shape[2] == 4:  # If image has alpha channel
        alpha_channel = img[:, :, 3]
        rgb_channels = img[:, :, :3]
        white_background = np.ones_like(rgb_channels, dtype=np.uint8) * 255
        alpha_factor = alpha_channel[:, :, np.newaxis] / 255.0
        img = rgb_channels * alpha_factor + white_background * (1 - alpha_factor)
        img = img.astype(np.uint8)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_resized = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)

    # Invert the image if needed (to ensure digits are white on black background)
    if np.mean(img_resized) > 127:
        img_resized = np.invert(img_resized)

    img_normalized = img_resized / 255.0
    img_input = np.expand_dims(img_normalized, axis=(0, -1))
    return img_input


def predict_digit(img):
    prediction = model.predict(img)
    digit = np.argmax(prediction)
    return digit


if __name__ == "__main__":
    app.run(debug=True)
