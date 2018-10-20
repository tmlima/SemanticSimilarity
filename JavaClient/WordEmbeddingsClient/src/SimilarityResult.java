import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class SimilarityResult {
	private String id;
	private String id_antecedent;
	private String similarity;
	
	public String getId() {
		return id;
	}
	
	public void setId(String id) {
		this.id = id;
	}
	
	public String getId_antecedent() {
		return id_antecedent;
	}
	
	public void setId_antecedent(String id_antecedent) {
		this.id_antecedent = id_antecedent;
	}
	
	public String getSimilarity() {
		return similarity;
	}
	
	public void setSimilarity(String similarity) {
		this.similarity = similarity;
	}	
}
