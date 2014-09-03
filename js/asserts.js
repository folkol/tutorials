
assert = function(message, condition) {
    if(condition) {
        document.write('<p class="success">SUCCESS! - ' + message +'</p>');
    } else {
        document.write('<p class="fail">FAILED! - ' + message + '</p>');
    }
}