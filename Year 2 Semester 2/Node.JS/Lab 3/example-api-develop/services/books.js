const BasicService = require('./basic.js');
const { BooksRepository } = require('../repositories/index.js');
const { Book, BookSchema } = require('../models/index.js');

const booksRepository = new BooksRepository();

class BooksService extends BasicService {
  constructor() {
    super(booksRepository, Book, BookSchema);
  }
}

module.exports = BooksService;
