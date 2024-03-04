window.onload = addUser;

function addUser() {
    var buttonName = document.getElementById("addUser");
    buttonName.onclick = handleButtonClick;
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
    else if (repeatPassword !== userPassword || repeatPassword == "") {
        alert("Пароли не совпадают! Повторите попытку!");
        var clearRepeatPassword = document.getElementById("repeatPassword");
        clearRepeatPassword.value = "";
        return false;
    }
    else {
        alert("Поздравляем, " + userName + ", регистрация завершена!")
    }
}
