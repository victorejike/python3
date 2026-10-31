import os
import re
from gensim.models import Word2Vec

class DesignSystemCorpus:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def __iter__(self):
        for root, _, files in os.walk(self.directory_path):
            for file in files:
                if file.endswith(('.md', '.txt', '.json')):
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        for line in f:
                            clean_line = re.sub(r'[^a-zA-Z0-9\s-]', '', line.lower())
                            tokens = clean_line.split()
                            if tokens:
                                yield tokens


DESIGN_DOCS_DIR = "./my_design_system_docs"
MODEL_PATH = "design_system_word2vec.model"


corpus = DesignSystemCorpus(DESIGN_DOCS_DIR)

if not os.path.exists(MODEL_PATH):
    print("Training initial model...")
    model = Word2Vec(vector_size=100, window=5, min_count=1, workers=4)
    
    model.build_vocab(corpus)
    
    if len(model.wv.key_to_index) == 0:
        print(f"\n❌ Error: No text data found in '{DESIGN_DOCS_DIR}'.")
        print("Please check that your folder contains .md, .txt, or .json files with actual words.")
    else:
        model.train(corpus, total_examples=model.corpus_count, epochs=5)
        model.save(MODEL_PATH)
        print("Gensim has successfully learned your design system vocabulary!")
else:
    print("Loading existing model...")
    model = Word2Vec.load(MODEL_PATH)
