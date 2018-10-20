import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class CandidatePair {
	private String id;
	private String lemma;	
	private String id_antecedent;
	private String lemma_antecedent;

	public CandidatePair(int id, String lemma, int idAntecedent, String lemmaAntecedent) {
		this.id = Integer.toString(id);
		this.lemma = lemma;
		this.id_antecedent = Integer.toString(idAntecedent);
		this.lemma_antecedent = lemmaAntecedent;
	}

	public String getId() {
		return id;
	}

	public String getLemma() {
		return lemma;
	}

	public String getid_antecedent() {
		return id_antecedent;
	}

	public String getlemma_antecedent() {
		return lemma_antecedent;
	}
}
