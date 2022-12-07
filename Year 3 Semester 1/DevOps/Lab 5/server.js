'use strict';

const express = require('express');

const PORT = 80;
const HOST = '0.0.0.0';

const app = express();
app.get('/', (request, response) => {
  response.send('<h2 style="color: red"> Hello world? I guess?<h2>');
});

app.listen(PORT, HOST);
console.log(`Yup, im runnin' on http://${HOST}:${PORT}`);
