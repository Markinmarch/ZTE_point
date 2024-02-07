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
    }
    else if (repeatPassword !== userPassword) {
        alert("Пароли не совпадают! Повторите попытку!");
    }
    else {
        alert(userName + ", регистрация прошла успешно!");
    }
}
