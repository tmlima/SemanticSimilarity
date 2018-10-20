import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.GenericType;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

public class Main {

	public static void main(String[] args) {

		Client client = ClientBuilder.newClient();  
		WebTarget target = client.target("http://127.0.0.1:5000/similarity");

		List<CandidatePair> pairs = new ArrayList<CandidatePair>();
		pairs.add(new CandidatePair(18, "final", 15, "conquista"));
		pairs.add(new CandidatePair(37, "fase", 12, "título"));
		
		Response response = target.request(MediaType.APPLICATION_JSON).post(Entity.json(pairs));
		List<SimilarityResult> results = response.readEntity(new GenericType<List<SimilarityResult>>() {});
		System.out.println(results.get(0).getSimilarity());
	}
}
