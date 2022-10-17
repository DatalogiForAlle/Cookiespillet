var checkbox1 = document.querySelector("input[name=a]");
var checkbox2 = document.querySelector("input[name=b]");
var checkbox3 = document.querySelector("input[name=c]");
var checkbox4 = document.querySelector("input[name=d]");
var checkbox5 = document.querySelector("input[name=e]");
var checkbox6 = document.querySelector("input[name=f]");
var checkbox7 = document.querySelector("input[name=g]");
var checkbox8 = document.querySelector("input[name=h]");

checkbox1.checked = true
checkbox2.checked = false
checkbox3.checked = false
checkbox4.checked = true
checkbox5.checked = true
checkbox6.checked = false
checkbox7.checked = true
checkbox8.checked = false


var list = [checkbox1, checkbox2, checkbox3, checkbox4, checkbox5, checkbox6, checkbox7, checkbox8]

checkbox1.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox1.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox1.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox1.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});

checkbox2.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox2.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox2.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox2.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});

checkbox3.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox3.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox3.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox3.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});

checkbox4.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox1.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox4.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox4.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});

checkbox5.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox1.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox5.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox5.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});

checkbox6.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox6.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox6.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox6.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});

checkbox7.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox7.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox7.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox7.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});


checkbox8.addEventListener('change', function () {
    console.log("Change seen")
    if (checkbox8.checked) {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == true) {
                list[i].checked = false
            } else {
                list[i].checked = true
            }
        }
        checkbox8.checked = false
    } else {
        for (let i = 0; i < list.length; i++) {
            if (list[i].checked == false) {
                list[i].checked = true
            } else {
                list[i].checked = false
            }
        }
        checkbox8.checked = true
    }
    if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked && !checkbox4.checked && !checkbox5.checked && !checkbox6.checked && !checkbox7.checked && !checkbox8.checked) {
        console.log("NO CHECKED BOXES");
        document.getElementById("send").value = 1;
        console.log(document.getElementById("send").value)
    }
});






