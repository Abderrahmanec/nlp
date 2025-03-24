# Project Documentation

## Overview
This project focuses on exploring and learning Natural Language Processing (NLP) concepts using Python libraries such as NLTK, SpaCy, and TensorFlow. It includes essential tasks like tokenization, text classification, word embeddings, and more advanced topics like neural networks and transformers.

## Project Structure

- **`README.md`**: Provides an introduction, project goals, and an overview of the project structure.
- **`datasets/`**: Contains datasets used for training and testing the models.
- **`src/`**: Contains the source code for different NLP tasks:
  - `tokenization.py`: Code for tokenizing text into words and sentences.
  - `text_classification.py`: Code for training and evaluating text classification models.
  - `embeddings.py`: Code for word embeddings like Word2Vec and GloVe.
- **`notebooks/`**: Jupyter notebooks for learning and experimentation:
  - `lesson_1_tokenization.ipynb`: Introduction to tokenization with examples.
  - `lesson_2_classification.ipynb`: Building and evaluating a text classification model.
- **`models/`**: Trained models:
  - `model_1.pkl`: A trained classification model.
  - `model_2.pkl`: A trained model for sentiment analysis.
- **`requirements.txt`**: List of dependencies required to run the project.
- **`utils/`**: Helper functions for tasks like data preprocessing and model evaluation.
- **`docs/`**: Additional documentation for understanding the project in detail.

## How to Run the Project
### Prerequisites
Make sure you have Python 3.x installed and the necessary libraries from the `requirements.txt` file:
```bash
pip install -r requirements.txt
