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
    // var accountStatus = "{{ data.status }}"
    // alert(accountStatus.status)

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
    // else if (accountStatus.status == "email_is_busy") {
    //     alert("Указанная электронная почта уже зарегестрирована, укажите другой адрес.")
    //     var clearUserEmail = document.getElementById("userEmail");
    //     clearUserEmail.value = "";
    //     return false;
    // }
    else {
        // alert(accountStatus)
        alert(userName + ", регистрация прошла успешно!");
    }
}
