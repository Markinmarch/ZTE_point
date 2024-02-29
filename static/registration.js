window.onload = addUser;

function addUser() {
    var checkStatus = new URLSearchParams(window.location.search);
    var status = checkStatus.get("status");
    var buttonName = document.getElementById("addUser");
    if (status == "email_is_busy") {
        alert("Указанная электронная почта уже зарегестрирована, укажите другой адрес.");
        window.location.replace("http://localhost:5000/registration");
    }
    else {
        buttonName.onclick = handleButtonClick;
    }
}

function handleButtonClick() {

    var userName = document.getElementById("userName").value;
    var userPhone = document.getElementById("userPhone").value;
    var userEmail = document.getElementById("userEmail").value;
    var userPassword = document.getElementById("userPassword").value;
    var repeatPassword = document.getElementById("repeatPassword").value;

    if (userName == "" || userPhone == "" || userEmail == "" || userPassword == "") {
        alert("Введите параметры, пожалуйста!");
        return false;
    }
    else if (repeatPassword !== userPassword) {
        alert("Пароли не совпадают! Повторите попытку!");
        var clearRepeatPassword = document.getElementById("repeatPassword");
        clearRepeatPassword.value = "";
        return false;
    }
}
