window.onload = addUser;

function addUser() {
    var buttonName = document.getElementById("addUser");
    buttonName.onclick = getUserRegistration;
}

function getUserRegistration() {
    var userName = document.getElementById("userName");
    var userPhone = document.getElementById("userPhone");
    var userEmail = document.getElementById("userEmail");
    var userPassword = document.getElementById("userPassword");
    var repeatPassword = document.getElementById("repeatPassword");

    var userData = JSON.stringify({
        email: userEmail.value,
        name: userName.value,
        phone: userPhone.value,
        password: userPassword.value
    });

    if (userName.value == "" || userPhone.value == "" || userEmail.value == "" || userPassword.value == "") {
        alert("Введите параметры, пожалуйста!");
        return false;
    }
    if (repeatPassword.value !== userPassword.value || repeatPassword.value == "") {
        alert("Пароли не совпадают! Повторите попытку!");
        repeatPassword.value = "";
        return false;
    }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/registration", true);
    xhr.setRequestHeader('content-type', 'application/json; charset=UTF-8');
    xhr.send(userData);
    xhr.onload = function() {
        if (xhr.response == "false") {
            alert("Адрес почты "+ userEmail.value + " уже зарегестрирован. Используйте другой.");
            userEmail.value = "";
        }
        else {
            alert("Поздравляем, " + userName.value + ", регистрация завершена!");
            window.location.replace("http://localhost:5000");
        }
    }
    
}
