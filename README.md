
# Handwritten Digit Recognizer

### About Handwritten Digits

Handwritten digits recognition is a fundamental problem in the field of machine learning and computer vision. The MNIST dataset, used extensively in this project, consists of 60,000 training images and 10,000 test images of handwritten digits from 0 to 9. Each image is grayscale and 28x28 pixels in size.

The goal of this project is to train a Convolutional Neural Network (CNN) model to accurately classify these handwritten digits. CNNs are particularly effective for image classification tasks due to their ability to learn hierarchical features directly from pixel data.

The MNIST dataset has been a benchmark for evaluating machine learning models for decades, providing a standard dataset for researchers and practitioners to compare and improve algorithms for handwritten digit recognition. By deploying this model as a web service, users can easily interact with it, uploading images of handwritten digits to receive real-time predictions.

This project demonstrates how machine learning can be applied to recognize and classify handwritten digits, showcasing the practical applications of deep learning in image recognition tasks.

## OUR GOAL

Our goal is to correctly identify digits from a dataset of tens of thousands of handwritten images. We’ve curated a set of tutorial-style kernels which cover everything from regression to neural networks. We encourage you to experiment with different algorithms to learn first-hand what works well and how techniques compare.


## Features

- **CNN Model:** Trains a TensorFlow/Keras CNN on the MNIST dataset.
- **Flask API:** Provides a web API endpoint for real-time predictions.
- **Heroku Deployment:** Hosts the model as a web service on Heroku.

## Getting Started

### Prerequisites

- Python 3.x
- Install required libraries:

  ```bash
  pip install -r requirements.txt
