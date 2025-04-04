import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os

# Define the corpus
corpus = [
    "Artificial Intelligence is transforming the world",
    "I am learning Natural Language Processing",
    "AI and NLP are exciting fields of study",
    "Machine learning powers many AI applications",
    "Deep learning is a subset of machine learning"
]

# Create vectorizers
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(corpus)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Feature names
bow_features = bow_vectorizer.get_feature_names_out()
tfidf_features = tfidf_vectorizer.get_feature_names_out()

# Create output folder
os.makedirs("figures", exist_ok=True)

# Plot BoW matrix
plt.figure(figsize=(12, 6))
sns.heatmap(bow_matrix.toarray(), annot=True, cmap="Blues",
            xticklabels=bow_features,
            yticklabels=[f"Sentence {i+1}" for i in range(len(corpus))])
plt.title("Bag of Words (BoW) Matrix")
plt.xlabel("Words")
plt.ylabel("Sentences")
plt.tight_layout()
plt.savefig("figures/bow_matrix.png")
plt.show()

# Plot TF-IDF matrix
plt.figure(figsize=(12, 6))
sns.heatmap(tfidf_matrix.toarray(), annot=True, cmap="YlGnBu",
            xticklabels=tfidf_features,
            yticklabels=[f"Sentence {i+1}" for i in range(len(corpus))])
plt.title("TF-IDF Matrix")
plt.xlabel("Words")
plt.ylabel("Sentences")
plt.tight_layout()
plt.savefig("figures/tfidf_matrix.png")
plt.show()
