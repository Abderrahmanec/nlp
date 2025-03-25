import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

# Read text from file
with open("datasets/text_for_processing.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tokenize the text into words
words = word_tokenize(text)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Create a dictionary with original words and their lemmatized versions
lemmatization_results = {"Original Word": words, "Lemmatized Word": [lemmatizer.lemmatize(word) for word in words]}

# Convert dictionary to a pandas DataFrame
df = pd.DataFrame(lemmatization_results)

# Save as a table in a CSV file
df.to_csv("datasets/lemmatization_result.csv", index=False)

# Print confirmation message
print("Lemmatization results saved in 'datasets/lemmatization_result.csv'")
print(df.head())  # Show first few rows
