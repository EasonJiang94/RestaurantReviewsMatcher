# This is for INFSCI 2440 in Spring 2024
# Please add comments with your code

# from gensim.models import Word2Vec
import gensim.models.keyedvectors as word2vec


path_to_word2vec="assign4_word2vec_for_python.bin"
path_to_word2vec_txt="data//assign4_reviews.txt"
embed_map = word2vec.KeyedVectors.load_word2vec_format(path_to_word2vec_txt, binary=True)
print(embed_map.similarity('great', 'good'))
print(embed_map.similarity('great', 'in'))


embed_map.save_word2vec_format(path_to_word2vec_txt, binary=True)