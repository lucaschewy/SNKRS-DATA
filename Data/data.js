const SneaksAPI = require('sneaks-api');
fs = require("fs");
const Papa = require("papaparse");
const sneaks = new SneaksAPI();



sneaks.getMostPopular(10000, function(err,products){

  var data = ""

  for(key in products){
    const generalData = JSON.stringify(products[key])
    const obj = JSON.parse(generalData);
    const priceData = JSON.stringify(products[key].lowestResellPrice)
    const obj2 = JSON.parse(priceData);
    const result = Object.assign({}, obj2, obj);
    const stringResult = JSON.stringify(result)
    if(data == ''){
      data = "[" + stringResult
    }else{
      data = data + "," + stringResult
    }
  }

  data = data + "]" 
  
  try {
    var csv_data = Papa.unparse(data);
    fs.writeFile("export.csv", csv_data, { flag: 'w' }, function(){});
  } catch(e){
      console.error(e);
  }

  console.log("--------------------------------------------------------------------------------------------------------------------")
  console.log("--------------------------------------------------------------------------------------------------------------------")
  console.log("Ne pas prêter attention aux erreurs en haut, ce n'est pas ma faute")
})