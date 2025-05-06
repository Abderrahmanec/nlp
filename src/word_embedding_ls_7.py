import nltk
from nltk.corpus import brown
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec, FastText

# Download the Brown corpus
nltk.download('brown')
sentences = brown.sents()

# Train CBOW, Skip-Gram, and FastText models
def train_models(sentences):
    print("Training Word2Vec CBOW...")
    cbow = Word2Vec(sentences, vector_size=100, window=5, min_count=2, sg=0)

    print("Training Word2Vec Skip-Gram...")
    skipgram = Word2Vec(sentences, vector_size=100, window=5, min_count=2, sg=1)

    print("Training FastText...")
    fasttext = FastText(sentences, vector_size=100, window=5, min_count=2)

    return cbow, skipgram, fasttext

# Visualize word embeddings using PCA
def visualize_embeddings(models, words, titles):
    plt.figure(figsize=(15, 5))

    for i, (name, model) in enumerate(models.items()):
        word_vectors = []
        labels = []

        for word in words:
            if word in model:
                word_vectors.append(model[word])
                labels.append(word)

        pca = PCA(n_components=2)
        reduced = pca.fit_transform(word_vectors)

        plt.subplot(1, 3, i + 1)
        plt.scatter(reduced[:, 0], reduced[:, 1], edgecolors='k')

        for label, x, y in zip(labels, reduced[:, 0], reduced[:, 1]):
            plt.annotate(label, (x, y))

        plt.title(titles[i])
        plt.grid(True)

    plt.tight_layout()
    plt.show()

# Main workflow
cbow_model, skipgram_model, fasttext_model = train_models(sentences)

# Words to compare visually
target_words = ['king', 'queen', 'man', 'woman', 'dog', 'cat', 'car', 'road', 'city', 'village']

# Collect models for plotting
models = {
    'CBOW': cbow_model.wv,
    'Skip-Gram': skipgram_model.wv,
    'FastText': fasttext_model.wv,
}

titles = ['Word2Vec CBOW', 'Word2Vec Skip-Gram', 'FastText']

# Run visualization
visualize_embeddings(models, target_words, titles)
