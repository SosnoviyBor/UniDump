const BasicService = require('./basic.js');
const { BookTypesRepository } = require('../repositories/index.js');
const { BookType, BookTypeSchema } = require('../models/index.js');

const bookTypesRepository = new BookTypesRepository();

class BookTypesService extends BasicService {
  constructor() {
    super(bookTypesRepository, BookType, BookTypeSchema);
  }
}

module.exports = BookTypesService;
