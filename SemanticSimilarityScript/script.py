from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format("Resource\\skip_s300.txt", unicode_errors="ignore")

print(model.most_similar("rei"))
