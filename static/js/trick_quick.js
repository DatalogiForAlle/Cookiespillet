var timeleft = 10;
var countdown = setInterval(function () {
    if (timeleft <= 0) {
        clearInterval(countdown);
    }
    makeAlert()
    timeleft -= 1;
}, 2000);


function makeAlert() {
    alert("Du skal være hurtig ;)");
};

