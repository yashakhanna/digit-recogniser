import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import sys

# Load the model
model = load_model('mnist_cnn_model.h5')

def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = img_array.reshape((1, 28, 28, 1))
    return img_array

def predict_digit(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)
    digit = np.argmax(predictions)
    return digit

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mnist_inference.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        digit = predict_digit(image_path)
        print(f"Predicted digit: {digit}")
