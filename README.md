# Semantic Similarity Web API
A Web API which calculates word similarity between words pairs

# Installation steps:
1. Install Python and PIP

* Linux

  `sudo apt install python3`

  `sudo apt install python3-pip`

2. Install required libraries

* `pip3 install -r requirements.txt`

3. Download model from NILC 

* http://nilc.icmc.usp.br/embeddings

4. Paste the file into `SemanticSimilarityScript/Resource/` folder

5. Set the file name in `word_embeddings_api.py` (default is `cbow_s300.txt`)

* `model = KeyedVectors.load_word2vec_format("Resource/cbow_s300.txt", unicode_errors="ignore")`

6. Run the server (it will take about three minutes to load the model)

* `python3 word_embeddings_api.py`

# Request example

```json
[
    {
        "id": "18",
        "lemma": "começo",
        "id_antecedent": "15",
        "lemma_antecedent": "início"
    },
    {
        "id": "37",
        "lemma": "maneira",
        "id_antecedent": "12",
        "lemma_antecedent": "forma"
    }
]
```

# Response example

```json
[
    {
        "id": "18",
        "id_antecedent": "15",
        "similarity": "0.84969133"
    },
    {
        "id": "37",
        "id_antecedent": "12",
        "similarity": "0.8975464"
    }
]
```
