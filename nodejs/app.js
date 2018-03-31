// Main module

// function sayHello(name) {
// 	console.log(`Hello ${name}!`);  // or global.console.log...
// }

// sayHello('Folkol');

console.log(module);  // NOT global.module

const logger = require('./logger');
console.log(logger);
logger.log('wut');

