# This is for INFSCI 2440 in Spring 2024
# Please add comments with your code
# Task 1: Extract opinion 

# import StringDouble
# import ExtractGraph

try:
    import stanza 
except ImportError:
    import pip
    pip.main(["install", "stanza"])
    import stanza 

# if you haven't downloaded the english package of stanza,
# please uncomment the following line to download it!
# stanza.download('en')

class ExtractOpinions:
    # Extracted opinions and corresponding review id is saved in extracted_pairs, where KEY is the opinion and VALUE
    # is the set of review_ids where the opinion is extracted from.
    # Opinion should in form of "attribute, assessment", such as "service, good".

    def __init__(self):
        # Initialize the NLP pipeline
        self.nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
        self.extracted_opinions = {}

    def extract_pairs(self, review_id, review_content):
        # Analyze the review content using NLP to extract opinions
        doc = self.nlp(review_content)
        for sentence in doc.sentences:
            for word in sentence.words:
                # Check for adjective modifiers (amod) related to a noun
                if word.deprel == 'amod' and sentence.words[word.head - 1].upos == 'NOUN':
                    attribute = sentence.words[word.head - 1].lemma
                    assessment = word.lemma
                    opinion = f"{attribute}, {assessment}"
                    if opinion in self.extracted_opinions:
                        if review_id not in self.extracted_opinions[opinion]:
                            self.extracted_opinions[opinion].append(review_id)
                    else:
                        self.extracted_opinions[opinion] = [review_id]

                # You might want to expand this section with more rules depending on the NLP analysis
                # For example, handling nominal subjects or compound modifiers

    def add_review(self, review_id, review_content):
        # This method will be called to process each review
        self.extract_pairs(review_id, review_content)


if __name__ == "__main__":
    extractor = ExtractOpinions()
    extractor.add_review(1, "The service is good and the food is excellent.")
    extractor.add_review(2, "The menu is large, the portions are even larger, and the prices are reasonable.")
    print(extractor.extracted_opinions)