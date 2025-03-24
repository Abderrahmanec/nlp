# Tokenization code
# src/tokenization.py
from nltk.tokenize import word_tokenize

# Read training data from datasets folder
with open('datasets/tokenization_description.txt', 'r') as file:
    text = file.read()

# Tokenization
tokens = word_tokenize(text)

# Save tokenized output
with open('datasets/tokenized_train.txt', 'w') as file:
    file.write("\n".join(tokens))

print("Tokenization completed and saved in datasets/tokenized_train.txt")
