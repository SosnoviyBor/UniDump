const BasicService = require('./basic.js');
const { AuthorsRepository } = require('../repositories/index.js');
const { Author, AuthorSchema } = require('../models/index.js');

const authorsRepository = new AuthorsRepository();

class AuthorsService extends BasicService {
  constructor() {
    super(authorsRepository, Author, AuthorSchema);
  }
}

module.exports = AuthorsService;
