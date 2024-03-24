window.onload = joinUser;

function joinUser() {
    var buttonName = document.getElementById("joinUser");
    buttonName.onclick = getUserJoin;
}

function getUserJoin() {
    var userEmail = document.getElementById("userEmail");
    var userPassword = document.getElementById("userPassword");
    
    var loginData = JSON.stringify({
        email: userEmail.value,
        password: userPassword.value
    });

    // if (userEmail == "" || userPassword == "") {
    //     alert("Введите параметры, пожалуйста!");
    //     return false;
    // }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
    xhr.setRequestHeader('content-type', 'application/json; charset=UTF-8');
    xhr.send(loginData);
    xhr.onload = function() {
        if (xhr.response == "false") {
            alert("Адрес почты или пароль не верны, повторите попытку.");
            // var clearUserEmail = document.getElementById("userEmail");
            // var clearUserPassword = document.getElementById("userPassword")
            userEmail.value = "";
            userPassword.value = "";
        }
        // else {
            // alert("Поздравляем, " + userName + ", регистрация завершена!");
            // window.location.replace("http://localhost:5000");
        // }
    }
}