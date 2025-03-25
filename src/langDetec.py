from langdetect import detect

# Example text in French
text = "Bonjour tout le monde!"
text2="أهلا و مرحبا بكم"
text3="Guten Tag!"

# Detect the language
language = detect(text)
print("Detected Language:", language)

language = detect(text2)

print("Detected Language:", language)

language = detect(text3)

print("Detected Language:", language)