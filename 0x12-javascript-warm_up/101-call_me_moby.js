#!/usr/bin/node

exports.callMeMoby = function (variable, callback) {
  for (let i = 0; i < variable; i++) {
    callback(variable);
  }
};
