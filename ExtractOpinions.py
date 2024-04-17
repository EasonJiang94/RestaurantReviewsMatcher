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
    extracted_opinions = {}

    def __init__(self):
        try : 
            self.nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
        except :
            stanza.download('en')
            self.nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
        return

    def extract_pairs(self, review_id, review_content):
        # example data, which you will need to remove in your real code. Only for demo.
        self.extracted_opinions = {'service, good': [1, 2, 5], 'service, excellent': [4, 6]}


if __name__ == "__main__":
    extractor = ExtractOpinions()
    extractor.add_review(1, "The service is good and the food is excellent.")
    extractor.add_review(2, "The menu is large, the portions are even larger, and the prices are reasonable.")
    print(extractor.extracted_opinions)