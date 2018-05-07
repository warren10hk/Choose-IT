var express = require('express');
var router = express.Router();

/* GET phonelist. */
router.get('/phonelist', function(req, res) {
  var db = req.db;
  var collection = db.get('phonelist');
  collection.find({},{},function(e,docs){
    res.json(docs);
  });
});

// /* POST to addphone. */
// router.post('/addphone', function(req, res) {
//   var db = req.db;
//   var collection = db.get('phonelist');
//   collection.insert(req.body, function(err, result){
//     res.send(
//       (err === null) ? { msg: '' } : { msg: err }
//     );
//   });
// });

// /* DELETE to deletephone. */
// router.delete('/deletephone/:id', function(req, res) {
//   var db = req.db;
//   var collection = db.get('phonelist');
//   var phoneToDelete = req.params.id;
//   collection.remove({ '_id' : phoneToDelete }, function(err) {
//     res.send((err === null) ? { msg: '' } : { msg:'error: ' + err });
//   });
// });

module.exports = router;