const http = require('http');
const url = require('url');

var cheminAccueil = "accueil.html"

http.createServer(function (requete, reponse) {
  reponse.write(requete.url);
  reponse.write(url.parse(requete.url).pathname);
  if ( url == "acceuil.html") {
    reponse.writeHead(200);
    reponse.end('Page found but has no point.');
  } else {
    reponse.writeHead(404);
    reponse.end('Page not found');
  }


}).listen(8080);
