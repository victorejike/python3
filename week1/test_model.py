from gensim.models import Word2Vec

# 1. Load the model you just trained
model = Word2Vec.load("design_system_word2vec.model")

# 2. Look up a word to find its semantically closest design terms
target_word = "button"

try:
    similar_words = model.wv.most_similar(target_word, topn=3)
    print(f"\nWords most closely related to '{target_word}':")
    for word, similarity in similar_words:
        print(f" - {word}: {similarity:.4f}")
except KeyError:
    print(f"\nThe word '{target_word}' wasn't found in your design documentation vocabulary yet.")
