from nltk import ngrams
from nltk.tokenize import word_tokenize

# Sample text
text = "This is an example sentence for n-gram creation."

# Tokenize the text
tokens = word_tokenize(text)

# Create bigrams (n=2)
bigrams = list(ngrams(tokens, 2))
print("Bigrams:", bigrams)
