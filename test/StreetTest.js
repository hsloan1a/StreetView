var streetView = require('../StreetView');
var assert = require('assert');


describe('Google Street View', function() {


  // describe('My Google Street View', function() {
  //   it('get image', function(done) {
  //     assert.deepEqual(streetView.StreetView(32.7830600, -96.8067800), 
  //       null);
  //     done();
  //   });

  //   });

  //different location
  describe('My Google Street View', function() {
    it('get image', function(done) {
      assert.deepEqual(streetView.StreetView(32.7840600, -96.8067800), 
        null);
      done();
    });

    });

});

