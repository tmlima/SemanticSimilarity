class Candidates:
    def __init__(self,  sn_id, sn_lemma, sn_id_antecedent, sn_lemma_antecedent):
        self.sn_id = sn_id
        self.sn_lemma = sn_lemma
        self.sn_id_antecedent = sn_id_antecedent
        self.sn_lemma_antecedent = sn_lemma_antecedent

    @classmethod
    def fromfile(self, line):
        sn = line.split("|")[0]
        snAntecedent = line.split("|")[1]
        return self(int(sn.split(" ")[0]), sn.split(" ")[1], int(snAntecedent.split(" ")[0]), snAntecedent.split(" ")[1])
