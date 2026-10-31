import os
from gensim.models import Word2Vec

MODEL_PATH = "design_system_word2vec.model"

# 1. Check if the model exists before loading
if not os.path.exists(MODEL_PATH):
    print(f"❌ Error: Model file '{MODEL_PATH}' not found. Please run design_model.py first.")
    exit()

# 2. Load your trained design system model
model = Word2Vec.load(MODEL_PATH)

# 3. Ask the user for a word to look up
word_to_check = input("Enter a word from your design system (e.g., button, color, brand): ").lower().strip()

print(f"\nSearching for terms closest to '{word_to_check}'...")

try:
    # 4. Find the top 5 most similar words
    similar_words = model.wv.most_similar(word_to_check, topn=5)
    
    print("\n✅ Closest matches found in your documentation:")
    for rank, (word, score) in enumerate(similar_words, 1):
        # score is a percentage of match from 0.0 to 1.0 (or 0% to 100%)
        print(f" {rank}. {word} ({score * 100:.1f}% match)")

except KeyError:
    print(f"\n❌ The word '{word_to_check}' is not in your model's vocabulary.")
    print("Gensim only knows words that exist in your 'my_design_system_docs' files.")
    print(f"Current vocabulary size: {len(model.wv.key_to_index)} unique words.")
