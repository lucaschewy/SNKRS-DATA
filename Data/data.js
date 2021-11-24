const SneaksAPI = require('sneaks-api');
fs = require("fs");
const Papa = require("papaparse");
const sneaks = new SneaksAPI();



sneaks.getMostPopular(10000, function(err,products){
    console.log(products)
    const data = JSON.stringify(products);
    console.log(data)
    try {
        var csv_data = Papa.unparse(data);
        fs.writeFile("./export.csv", csv_data, { flag: 'w' }, function(){
          console.log(csv_data);
        });
      } catch(e){
        console.error(e);
      }
})

// éditer le fichier json pour éditer les objets et créer des nouveaux champs pour chaque entrée
// exporter en csv