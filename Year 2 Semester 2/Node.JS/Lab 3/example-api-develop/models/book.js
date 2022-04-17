const Joi = require('joi');
const Basic = require('./basic.js');

const BookSchema = Joi.object({
  title: Joi.string().trim().min(1).max(200).required(),
  author: Joi.string().uuid().required(),
  size: Joi.number().min(1).required(),
  type: Joi.string().uuid().required(),
});

class Book extends Basic {
  constructor({ title, author, size, type }) {
    super();
    this.title = title;
    this.author = author;
    this.size = size;
    this.type = type;
  }
}

module.exports = { Book, BookSchema };
