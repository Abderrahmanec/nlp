from textblob import TextBlob

# Read the text from the 'sentiment_analysis.txt' file
with open("datasets/sentiment_analysis.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create a TextBlob object from the text
blob = TextBlob(text)

# Get the sentiment of the text (polarity and subjectivity)
sentiment = blob.sentiment

# Multiply the polarity by 100 to get a score between -100 and 100
polarity_score = sentiment.polarity * 100

# Determine the sentiment type based on the polarity score
if polarity_score > 0:
    sentiment_type = "Positive"  # If the score is positive, the sentiment is Positive
elif polarity_score < 0:
    sentiment_type = "Negative"  # If the score is negative, the sentiment is Negative
else:
    sentiment_type = "Neutral"  # If the score is 0, the sentiment is Neutral

# Prepare the result text to write into a new file
result = f"Sentiment Analysis Results:\n\nText: {text}\n\nPolarity: {polarity_score}\nSentiment: {sentiment_type}"

# Write the result to a new file 'sentiment_analysis_result.txt'
with open("datasets/sentiment_analysis_result.txt", "w", encoding="utf-8") as result_file:
    result_file.write(result)

# Print a confirmation message
print("Sentiment analysis result has been saved to 'sentiment_analysis_result.txt'.")
