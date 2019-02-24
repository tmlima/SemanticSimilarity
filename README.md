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
