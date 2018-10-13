from gensim.models import KeyedVectors
from candidates import Candidates
from similar_candidates import SimilarCandidates

def calculate_similarity(candidate, model):
    if (candidate.sn_lemma in model.vocab and candidate.sn_lemma_antecedent in model.vocab):
        return float(model.similarity(candidate.sn_lemma, candidate.sn_lemma_antecedent))
    return 0

model = KeyedVectors.load_word2vec_format("Resource/glove_s50.txt", unicode_errors="ignore")
print("model loaded")

similar_candidates = []

path = "candidates/D1_C28_Folha_15-07-2007_17h12.txt"
with open(path, "r") as file:
    for line in file:
        line = line.replace("\n","")
        candidate = Candidates(line)
        similarity = calculate_similarity(candidate, model)
        if (similarity > 0.8):
            ca = SimilarCandidates(candidate.sn_id, candidate.sn_id_antecedent, similarity)
            similar_candidates.append(ca)

for c in similar_candidates:
    print(c.sn_id + c.sn_id_antecedent + c.similarity)

print("done")
