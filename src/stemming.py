import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

# Download necessary resources
nltk.download('punkt')

# Read the input text
with open("datasets/text_for_processing.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Initialize the stemmer
stemmer = PorterStemmer()
words = word_tokenize(text)

# Create a DataFrame to compare original words and stemmed words
df = pd.DataFrame({"Original Word": words, "Stemmed Word": [stemmer.stem(word) for word in words]})

# Save the result as a CSV file (tabular format)
df.to_csv("datasets/stemming_result.csv", index=False)

print("Stemming result saved in 'datasets/stemming_result.csv'")
