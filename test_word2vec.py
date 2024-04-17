# This is for INFSCI 2440 in Spring 2024
# Please add comments with your code

# from gensim.models import Word2Vec
import gensim.models.keyedvectors as word2vec

def show_sim(text1, text2):
    print(f"The similarity of '{text1}' and '{text2}' is {embed_map.similarity(text1, text2)}")

path_to_word2vec="assign4_word2vec_for_python.bin"
path_to_word2vec_txt="data/assign4_reviews.txt"
embed_map = word2vec.KeyedVectors.load_word2vec_format(path_to_word2vec, binary=True)
show_sim('good', 'great')
show_sim('good', 'bad')
show_sim('service', 'waiter')
show_sim('service', 'atmosphere')
show_sim('service', 'feeling')
show_sim('service', 'atmosphere')
show_sim('service', 'ambience')
show_sim('food', 'meal')
show_sim('delicious', 'interesting')
show_sim('delicious', 'hearty')
show_sim('delicious', 'fresh')
show_sim('good', 'delicious')
show_sim('good', 'hearty')
show_sim('good', 'fresh')
show_sim('good', 'interesting')
show_sim('bad', 'delicious')
show_sim('bad', 'hearty')
show_sim('bad', 'fresh')
show_sim('bad', 'interesting')


embed_map.save_word2vec_format(path_to_word2vec_txt, binary=True)