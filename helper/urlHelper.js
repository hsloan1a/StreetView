


////https://maps.googleapis.com/maps/api/streetview?size=600x300&location=32.7830600,-96.8067800&heading=151.78&pitch=-0.76&key=-UGovbUHAaUURj8UQlmM2KQV0

   const options = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'    
    }
  };


  module.exports = {

  setOptions: function (method, url){

  options.url = 'https://maps.googleapis.com/maps/api/streetview';
  options.method = method;


    return options;
  }


};
