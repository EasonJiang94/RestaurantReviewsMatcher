# This is for INFSCI 2440 in Spring 2024
# Please add comments with your code
# Main function for evaluation (DO NOT CHANGE)

import ExtractOpinions
import FindSimilarOpinions

# Step 1: Extract opinions from assign4_reviews.txt
step_1_extract_opinion = ExtractOpinions.ExtractOpinions()
review_id = 1
f = open('data/assign4_reviews.txt', 'r')
for line in open('data/assign4_reviews.txt'):
    review_content = f.readline()
    step_1_extract_opinion.extract_pairs(review_id, review_content)
    review_id = review_id + 1
f.close()

# Print extracted opinions
extracted_opinions = step_1_extract_opinion.extracted_opinions
for tmp_opinion in extracted_opinions:
    review_ids = extracted_opinions[tmp_opinion]
    print("\n[" + tmp_opinion + "] appears in review " + "\t" + " ".join(str(review_ids)))
print("\n--------------------------------------------------------------")
del(step_1_extract_opinion)
# Step 2: Find similar extracted opinions
cosine_sim = 0.8
step_2_find_similar_opinion = FindSimilarOpinions.FindSimilarOpinions(cosine_sim, extracted_opinions)
opinions = ["service, good", "service, bad", "atmosphere, good", "food, delicious"]
for query_opinion in opinions:
    print("\nquery opinion [" + query_opinion + "] has similar opinions: ")
    similar_opinions = step_2_find_similar_opinion.findSimilarOpinions(query_opinion)
    
    for tmp_opinion in similar_opinions:
        review_ids = similar_opinions[tmp_opinion]
        print("\n\t[" + tmp_opinion + "] appears in review " + "\t" + " ".join(str(review_ids)))
print("\n--------------------------------------------------------------")
