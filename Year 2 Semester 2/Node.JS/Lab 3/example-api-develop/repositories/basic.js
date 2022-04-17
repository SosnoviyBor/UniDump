class BasicRepository {
  constructor() {
    this.data = new Map();

    if (BasicRepository._instance) {
      return BasicRepository._instance;
    }

    BasicRepository._instance = this;
  }

  add(id, model) {
    this.data.set(id, model);
    return this.getById(id);
  }

  getById(id) {
    return this.data.get(id);
  }

  deleteById(id) {
    return this.data.delete(id);
  }

  updateById(id, value) {
    return this.data.set(id, value);
  }

  getAll() {
    return this.data.values();
  }

  findOne(query) {
    const models = this.getAll();

    for (const model of models) {
      if (this.areEqual(query, model)) {
        return model;
      }
    }

    return null;
  }

  findAll(query) {
    const models = this.getAll();
    const foundModels = [];

    for (const model of models) {
      if (this.areEqual(query, model)) {
        foundModels.push(model);
      }
    }

    return foundModels;
  }

  areEqual(query, model) {
    for (const key in query) {
      if (query[key] !== model[key]) {
        return false;
      }
    }

    return true;
  }
}

module.exports = BasicRepository;
