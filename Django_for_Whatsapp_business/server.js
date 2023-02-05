const express = require('express');

const app = express();

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "https://95b1-190-80-50-96.sa.ngrok.io/");
    next();
  });

  app.listen(5500, function() {
    console.log('Server listening on port 3000');
  });
    