class Candidates:
    def __init__(self, line):
        sn = line.split("|")[0]
        snAntecedent = line.split("|")[1]

        self.sn_id = int(sn.split(" ")[0])
        self.sn_lemma = sn.split(" ")[1]
        self.sn_id_antecedent = int(snAntecedent.split(" ")[0])
        self.sn_lemma_antecedent = snAntecedent.split(" ")[1]
