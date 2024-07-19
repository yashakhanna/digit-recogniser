# MNIST Digit Recognition

This repository contains a Convolutional Neural Network (CNN) model trained on the MNIST dataset for digit recognition.

## Files

- `mnist_cnn_model.h5`: The trained model.
- `mnist_inference.py`: Script to load the model and predict digits from images.
- `requirements.txt`: Required Python packages.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/haffy1/digit.git
    cd digit
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the inference script with the path to an image:
```sh
python mnist_inference.py "C:\Users\dhill\Downloads\MNIST Dataset JPG format\MNIST Dataset JPG format\MNIST - JPG - training\7\9788.jpg"

