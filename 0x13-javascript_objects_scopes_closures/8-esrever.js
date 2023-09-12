#!/usr/bin/node

exports.esrever = function (list) {
  const midOfList = Math.ceil(list.length / 2);
  let endOfList = list.length - 1;
  for (let i = 0; i !== midOfList; ++i) {
    let temp = list[i];
    list[i] = list[endOfList];
    list[endOfList] = temp;
    --endOfList;
  }
  return list;
};
