function submit() {
    document.getElementById("send").value = 0;
    document.forms[0].submit();
};

setInterval(submit, 7000);