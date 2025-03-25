from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to translate text
def translate_text(text, src_lang='en', dest_lang='fr'):
    """
    Function to translate text from the source language to the destination language.
    
    :param text: Text to be translated
    :param src_lang: Source language (default is 'en' for English)
    :param dest_lang: Destination language (default is 'fr' for french)
    :return: Translated text
    """
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

# Example usage: Translate from English to french
text_to_translate = "Hello, how are you?"
translated_text = translate_text(text_to_translate, src_lang='en', dest_lang='fr')

print(f"Original text: {text_to_translate}")
print(f"Translated text: {translated_text}")
