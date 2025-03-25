from collections import Counter
import nltk
nltk.download('punkt')



# Sample text for frequency analysis
text = "This is a simple text. This text is for word frequency analysis."

# Tokenize the text
words = nltk.word_tokenize(text)

# Count the frequency of each word
word_frequencies = Counter(words)
print("Word Frequencies:", word_frequencies)
