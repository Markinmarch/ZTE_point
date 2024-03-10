window.onload = addUser;

function addUser() {
    var buttonName = document.getElementById("addUser");
    buttonName.onclick = getUserRegistration;
}

function getUserRegistration() {

    var userName = document.getElementById("userName").value;
    var userPhone = document.getElementById("userPhone").value;
    var userEmail = document.getElementById("userEmail").value;
    var userPassword = document.getElementById("userPassword").value;
    var repeatPassword = document.getElementById("repeatPassword").value;

    var userData = JSON.stringify({
        email: userEmail,
        name: userName,
        phone: userPhone,
        password: userPassword
    });

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

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/registration", true);
    xhr.setRequestHeader('content-type', 'application/json; charset=UTF-8');
    xhr.send(userData);
    xhr.onload = function() {
        if (xhr.response == "false") {
            alert("Адрес почты "+ userEmail + " уже зарегестрирован. Используйте другой.");
            var clearUserEmail = document.getElementById("userEmail");
            clearUserEmail.value = "";
        }
        else {
            alert("Поздравляем, " + userName + ", регистрация завершена!");
            window.location.replace("http://localhost:5000");
        }
    }
    
}
