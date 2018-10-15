from flask import Flask, jsonify,  session, request
from gensim.models import KeyedVectors

print("loading")
model = KeyedVectors.load_word2vec_format("Resource/glove_s300.txt", unicode_errors="ignore")
print("model loaded")

app = Flask(__name__)

@app.route("/similarity", methods=['POST'])
def similarity():
    if request.method == 'POST':
        pairs = request.get_json()
        response = []
        for p in pairs:
            similarity = model.similarity(p["lemma"],  p["lemma_antecedent"])
            response.append({ 
                "id" : p["id"],
                "id_antecedent" : p["id_antecedent"],
                "similarity" : str(similarity) })
        return jsonify(response)
    
if __name__ == "__main__":
    app.run(debug=True)