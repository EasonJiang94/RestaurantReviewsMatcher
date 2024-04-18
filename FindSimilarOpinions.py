# This is for INFSCI 2440 in Spring 2024
# Please add comments with your code
# Task 2: Find similar opinions 

import gensim.models.keyedvectors as word2vec
import heapq


class FindSimilarOpinions:
    extracted_opinions = {}
    word2VecObject = []
    cosine_sim = 0

    def __init__(self, input_cosine_sim, input_extracted_ops):
        self.cosine_sim = input_cosine_sim
        self.extracted_opinions = input_extracted_ops
        self.recorded_noun = {}
        self.recorded_adj = {}
        word2vec_add = "assign4_word2vec_for_python.bin"
        self.word2VecObject = word2vec.KeyedVectors.load_word2vec_format(word2vec_add, binary=True)
    
    
    def get_word_sim(self, word_1, word_2):
        try:
            return self.word2VecObject.similarity(word_1, word_2)
        except KeyError:
            return 0

    def findSimilarOpinions(self, query_opinion):
        noun, adj = query_opinion.split(", ")
        top_15_sim_adj_good = []
        top_15_sim_adj_bad = []
        
        # Determine initial similarity of the query adjective to "good" and "bad"
        sim_to_good = self.get_word_sim(adj, "good")
        sim_to_bad = self.get_word_sim(adj, "bad")
        self.recorded_adj = {}
        # Iterate over each extracted opinion
        for extracted_opinion in self.extracted_opinions:
            _, ex_adj = extracted_opinion.split(", ")
            
            # Avoid recalculating for the same adjective
            if ex_adj in self.recorded_adj:
                continue
            self.recorded_adj[ex_adj] = True
            
            # Calculate similarity to "good" and "bad"
            ex_sim_to_good = self.get_word_sim(ex_adj, "good")
            ex_sim_to_bad = self.get_word_sim(ex_adj, "bad")
            
            # Classify the adjective based on which word it is closer to
            if ex_sim_to_good >= ex_sim_to_bad:
                heapq.heappush(top_15_sim_adj_good, (ex_sim_to_good, ex_adj))
                if len(top_15_sim_adj_good) > 15:
                    heapq.heappop(top_15_sim_adj_good)
            else:
                heapq.heappush(top_15_sim_adj_bad, (ex_sim_to_bad, ex_adj))
                if len(top_15_sim_adj_bad) > 15:
                    heapq.heappop(top_15_sim_adj_bad)
        
        # Output the closest group
        if sim_to_good >= sim_to_bad:
            closer_group = sorted(top_15_sim_adj_good, reverse=True, key=lambda x: x[0])
            print("Query is closer to 'good'. Similar adjectives:")
        else:
            closer_group = sorted(top_15_sim_adj_bad, reverse=True, key=lambda x: x[0])
            print("Query is closer to 'bad'. Similar adjectives:")
        
        for score, adjective in closer_group:
            print(f"{adjective}: {score}")

        return []
        example_similarity = self.get_word_sim("great", "good")
        similar_opinions = {'service, good': [1, 2, 3], 'service, excellent': [11, 12]}
        return similar_opinions
