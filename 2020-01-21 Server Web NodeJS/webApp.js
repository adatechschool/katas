const http = require('http');
const url = require('url');

var cheminAccueil = "accueil.html"
var nomHtml = url.pathname

console.log(nomHtml);

http.createServer(function (requete, reponse) {
var pathname =url.parse(requete.url).pathname;
console.log(pathname);
	// reponse.write(requete.url);
 // reponse.write(url.parse(requete.url).pathname);
  if ( pathname == "/") {
    reponse.writeHead(200);
    reponse.end('Page found but has no point.');
  } else {
    reponse.writeHead(404);
    reponse.end('Page not found');
  }

console.log(url.parse(requete.url).pathname);

}).listen(8080);
