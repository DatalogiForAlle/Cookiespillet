console.log("Hello World")

var checkbox1 = document.querySelector("input[name=a]");
var checkbox2 = document.querySelector("input[name=b]");
var checkbox3 = document.querySelector("input[name=c]");
var checkbox4 = document.querySelector("input[name=d]");

checkbox1.addEventListener('change', function () {
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});

checkbox2.addEventListener('change', function () {
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked) {
        document.getElementById("send").value = 1;
    }
});

checkbox3.addEventListener('change', function () {
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked) {
        document.getElementById("send").value = 1;
    }
});

checkbox4.addEventListener('change', function () {
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked) {
        document.getElementById("send").value = 1;
    }
});
