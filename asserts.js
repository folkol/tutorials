assert = function(message, condition) {
    if(condition) {
        document.write('<p class="success"></p>');
    } else {
        document.write('<p class="fail">FAILED! - ' + message + '</p>');
    }
}