// Main module

// function sayHello(name) {
// 	console.log(`Hello ${name}!`);  // or global.console.log...
// }

// sayHello('Folkol');

// console.log(module);  // NOT global.module

// const logger = require('./logger');
// console.log(logger);
// logger.log('wut');

const path = require('path');
const pathObj = path.parse(__filename);

console.log(pathObj);

