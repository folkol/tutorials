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

// const EventEmitter = require('events');
// const emitter = new EventEmitter();  // Not the same emitter as the one in logger.js...


// const Logger = require('./logger');
// const logger = new Logger();

// logger.on('messageLogged', console.log);

// logger.log('message');

const port = 1234;

const http = require('http');
const server = http.createServer((request, response) => {
	if(request.url === '/') {
		response.write('Hello, world!\n');
	}

	if(request.url === '/api/courses') {
		response.write(JSON.stringify([1, 2, 3]));
	}
	response.end();
});
server.listen(port);
console.log(`Listening on port http://localhost:${port}/`)
// server.on('connection', socket => console.log('New connection'));
