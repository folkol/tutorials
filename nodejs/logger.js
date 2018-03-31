const EventEmitter = require('events');

class Logger extends EventEmitter { // Syntactic sugar for constructor function
	log(message) {
		this.emit('messageLogged', { id: 1, url: message });
		// Send HTTP request
	}
}

module.exports = Logger;
