const {
  AuthorsService,
  BooksService,
  BookTypesService,
} = require('./services/index.js');

const authors = new AuthorsService();
const books = new BooksService();
const bookTypes = new BookTypesService();
