const Joi = require('joi');
const Basic = require('./basic.js');

const BookTypeSchema = Joi.object({
  name: Joi.string().trim().min(1).max(200).required(),
});

class BookType extends Basic {
  constructor({ name }) {
    super();
    this.name = name;
  }
}

module.exports = {
  BookType,
  BookTypeSchema,
};
