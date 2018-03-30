
//needed url 
//https://maps.googleapis.com/maps/api/streetview?size=600x300&location=32.7830600,-96.8067800&heading=151.78&pitch=-0.76&key=apikey
var fs = require('fs');
var uuidv4 = require('uuid/v4');
var request = require('request');
var urlHelper = require('./helper/urlHelper');


var download = function(uri, filename, callback){
  request.head(uri, function(err, res, body){
    console.log('content-type:', res.headers['content-type']);
    console.log('content-length:', res.headers['content-length']);

    request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
  });
};


module.exports = {

  StreetView: function (x, y){
    var key = "";
    var locationX = x;
    var locationY = y;
    for (var updatedPosition = 0; updatedPosition < 300; updatedPosition = updatedPosition + 20){
      download('https://maps.googleapis.com/maps/api/streetview?size=600x300&location='+locationX+','+locationY+'&heading=80&pitch=-0.76&key=' + key, 
        uuidv4() + '.png', function(){
       console.log('done');
      });
      locationY+=.00005;
    }
  }
};
