package tennis;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

public class TenniServer {

	public static void main(String[] args) throws Exception {
		HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
		server.createContext("/fayal", new MyHandler());
		server.setExecutor(null); // creates a default executor
		server.start();
	}

	static class MyHandler implements HttpHandler {
		@Override
		public void handle(HttpExchange t) throws IOException {
			Joueuse joueuse1 = new Joueuse("Lydia");
			Joueuse joueuse2 = new Joueuse("Del");

			String response = "This is the response";
			response += "\n Joueuse 1 : " + joueuse1.affiche();
			response += "\n Joueuse 2 : " + joueuse2.affiche();
			response += "\n joueuse 1 statique: " + joueuse1.afficheStatique();
			response += "\n joueuse 2 statique: " + joueuse2.afficheStatique();

			t.sendResponseHeaders(200, response.length());
			OutputStream os = t.getResponseBody();
			os.write(response.getBytes());
			os.close();
		}
	}

}


public class Joueuse {

	String nom;
	static String nomStatique;

	Joueuse(String nom) {
		this.nom = nom;
		this.nomStatique = nom;
	}

	String affiche() {
		return "coucou depuis Joueuse " + this.nom;
	}

	static String afficheStatique() {
		return "coucou depuis statique " + nomStatique;
	}
}
