#!/usr/bin/node
exports.addMeMaybe = function (variable, callback) {
  variable = variable + 1;
  callback(variable);
};
