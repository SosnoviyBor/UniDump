const Messages = require('../constants/messages.js');

class BasicService {
  constructor(repository, model, schema) {
    this.repository = repository;
    this.model = model;
    this.schema = schema;
  }

  add(entity) {
    const { error } = this.schema.validate(entity);

    if (error) {
      throw error;
    }

    const model = new this.model(entity);
    this.repository.add(model.id, model);

    return model;
  }

  getById(id) {
    const model = this.repository.getById(id);

    if (!model) {
      throw new Error(Messages.ERRORS.NOT_EXISTS('Entity'));
    }

    return model;
  }

  updateById(id, entity) {
    let model = this.repository.getById(id);

    if (!model) {
      throw new Error(Messages.ERRORS.NOT_EXISTS('Entity'));
    }

    const { error } = this.schema.validate(entity);

    if (error) {
      throw error;
    }

    model = new this.model(entity);
    model.id = id;
    this.repository.updateById(id, model);

    return model;
  }

  deleteById(id) {
    const model = this.repository.getById(id);

    if (!model) {
      throw new Error(Messages.ERRORS.NOT_EXISTS('Entity'));
    }

    this.repository.deleteById(id);
  }

  getAll() {
    return this.repository.getAll();
  }

  findOne(query) {
    return this.repository.findOne(query);
  }

  findAll(query) {
    return this.repository.findAll(query);
  }
}

module.exports = BasicService;
