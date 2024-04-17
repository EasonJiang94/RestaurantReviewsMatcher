# This is for INFSCI 2440 in Spring 2024
# Please add comments with your code
# Task 1: Extract opinion 

# import StringDouble
# import ExtractGraph
import json
try:
    from stanfordcorenlp import StanfordCoreNLP
except ImportError:
    import pip
    pip.main(["install", "stanfordcorenlp"])
    from stanfordcorenlp import StanfordCoreNLP


# if you haven't downloaded the english package of stanza,
# please uncomment the following line to download it!
# stanza.download('en')

class ExtractOpinions:
    # Extracted opinions and corresponding review id is saved in extracted_pairs, where KEY is the opinion and VALUE
    # is the set of review_ids where the opinion is extracted from.
    # Opinion should in form of "attribute, assessment", such as "service, good".
    extracted_opinions = {}

    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port, timeout=10)  # adjust port if different

        

    def extract_pairs(self, review_id, review_content):
        # Parse the sentence using the CoreNLP server
        props = {'annotators': 'tokenize,ssplit,pos,lemma,depparse', 'pipelineLanguage': 'en', 'outputFormat': 'json'}
        parsed = json.loads(self.nlp.annotate(review_content, properties=props))
        for i, sentence in enumerate(parsed['sentences']):
            # print(f"{sentence = }")
            for j, dep in enumerate(sentence['enhancedPlusPlusDependencies']):
                print(f"{review_id = }, {i = }, {j = }, {dep = }")
                if dep['dep'] == 'amod' and 'NN' in sentence['tokens'][dep['governor']-1]['pos']:
                    # Extract the noun and adjective
                    attribute = sentence['tokens'][dep['governor']-1]['lemma']
                    assessment = sentence['tokens'][dep['dependent']-1]['lemma']
                    opinion = f"{attribute}, {assessment}"
                    if opinion in self.extracted_opinions:
                        if review_id not in self.extracted_opinions[opinion]:
                            self.extracted_opinions[opinion].append(review_id)
                    else:
                        self.extracted_opinions[opinion] = [review_id]

    def close(self):
        self.nlp.close()

    def add_review(self, review_id, review_content):
        self.extract_pairs(review_id, review_content)


if __name__ == "__main__":
    extractor = ExtractOpinions()
    extractor.add_review(1, "The service is good and the food is excellent.")
    extractor.add_review(2, "The menu is large, the portions are even larger, and the prices are reasonable.")
    print(extractor.extracted_opinions)
    extractor.close()

    # step_1_extract_opinion = ExtractOpinions()
    # review_id = 1
    # f = open('data/assign4_reviews.txt', 'r')
    # for line in open('data/assign4_reviews.txt'):
    #     review_content = f.readline()
    #     step_1_extract_opinion.extract_pairs(review_id, review_content)
    #     review_id = review_id + 1
    # f.close()