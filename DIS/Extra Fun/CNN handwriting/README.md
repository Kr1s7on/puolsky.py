# Handwritten Digit Recognition with Flask and TensorFlow

This project is a web application for recognizing handwritten digits using a Convolutional Neural Network (CNN) built with TensorFlow and served using Flask. Users can draw a digit on a canvas, and the application will predict the digit.

## Features
- Web interface for drawing digits
- Preprocessing of images to ensure proper digit recognition
- TensorFlow model for digit classification
- REST API for making predictions

## Requirements
- Python 3.7 or higher

## Installation
1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Train the model:
    - Fill in the `build_model` function in `model.py` with your desired model architecture.
    - Run `model.py` to train and save the model:
      ```bash
      python model.py
      ```

2. Start the Flask app:
    ```bash
    python app.py
    ```

3. Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure
- `app.py`: Flask application to serve the web interface and handle image processing and predictions.
- `model.py`: Script to build, train, and save the TensorFlow model.
- `requirements.txt`: List of required Python packages.
- `templates/index.html`: HTML template for the web interface.

## Filling the `build_model` Function
The `build_model` function in `model.py` is where you define the architecture of your CNN. Here's an example of what this function might look like:

```python
def build_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    return model
``` 

## Objective
Figure out what each part of the model does and how it contributes to the overall architecture. You can experiment with different architectures to see how they affect the model's performance.

Look through some of these resources
- [Introduction to Convolutional Neural Networks for Visual Recognition](https://cs231n.github.io/convolutional-networks/)
- [Deep Learning Specialization by Andrew Ng on Coursera](https://www.coursera.org/specializations/deep-learning)
- [TensorFlow CNN Tutorial](https://www.tensorflow.org/tutorials/images/cnn)
- [A Beginner's Guide To Understanding Convolutional Neural Networks](https://towardsdatascience.com/a-beginners-guide-to-understanding-convolutional-neural-networks-6d0fbf5e5ef1)
