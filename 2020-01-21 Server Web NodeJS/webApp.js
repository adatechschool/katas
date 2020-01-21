var http = require('http');

var cheminAccueil = "accueil.html"

http.createServer(function (req, res) {
  res.write(cheminAccueil); 
  res.end();
}).listen(8080);
