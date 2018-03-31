// Main module

// function sayHello(name) {
// 	console.log(`Hello ${name}!`);  // or global.console.log...
// }

// sayHello('Folkol');

// console.log(module);  // NOT global.module

// const logger = require('./logger');
// console.log(logger);
// logger.log('wut');

// const path = require('path');
// const pathObj = path.parse(__filename);

// console.log(pathObj);

// const os = require('os');
// console.log(Object.keys(os));

// const totalMemory = os.totalmem();
// const freeMemory = os.freemem();

// console.log(`Total memory: ${totalMemory}, Free memory: ${freeMemory}`);

// const fs = require('fs');

// // const files = fs.readdirSync('.');
// // console.log(files);

// const files = fs.readdir('.', (err, files) => console.log('Result:', err || files));
// // console.log(files);

const EventEmitter = require('events');
const emitter = new EventEmitter();  // Not the same emitter as the one in logger.js...


const Logger = require('./logger');
const logger = new Logger();

logger.on('messageLogged', console.log);

logger.log('message');
