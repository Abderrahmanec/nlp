from textblob import TextBlob

# Example text with a spelling mistake
text = "I havv goood speling!"

# Create a TextBlob object
blob = TextBlob(text)

# Correct the spelling
corrected_text = blob.correct()
print("Corrected Text:", corrected_text)


#example 2
text2 = "I am a good speler!"   # The word 'speler' is misspelled
blob2 = TextBlob(text2)
corrected_text2 = blob2.correct()
print("Corrected Text:", corrected_text2)