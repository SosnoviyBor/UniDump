const { v4: uuid } = require('uuid');

class Basic {
  id = uuid();
}

module.exports = Basic;
