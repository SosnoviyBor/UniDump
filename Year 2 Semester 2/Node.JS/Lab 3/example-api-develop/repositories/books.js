const BasicRepository = require('./basic.js');
const BookTypesRepository = require('./book-types.js');
const AuthorsRepository = require('./authors.js');

const bookTypesRepository = new BookTypesRepository();
const authorsRepository = new AuthorsRepository();

class BooksRepository extends BasicRepository {
  getFullById(id) {
    const book = this.getById(id);
    const bookType = bookTypesRepository.getById(book.type);
    const author = authorsRepository.getById(book.author);

    book.type = bookType;
    book.author = author;

    return book;
  }
}

module.exports = BooksRepository;
