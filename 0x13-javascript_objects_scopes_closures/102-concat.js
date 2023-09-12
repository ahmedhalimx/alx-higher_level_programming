#!/usr/bin/node
const FS = require('fs');

const fArg = FS.readFileSync(process.argv[2]).toString();
const sArg = FS.readFileSync(process.argv[3]).toString();
FS.writeFileSync(process.argv[4], fArg + sArg);
