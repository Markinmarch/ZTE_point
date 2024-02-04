// window.onload = addUser;

function addUser() {
    var buttonName = document.getElementById("addUser");
    buttonName.onclick = handleButtonClick;
}

function handleButtonClick() {
    var textInputName = document.getElementsByName("userName");
    var userName = textInputName.value;
    var textInputPhone = document.getElementsByName("userPhone");
    var userPhone = textInputPhone.value;
    var textInputEmail = document.getElementsByName("userEmail");
    var userEmail = textInputEmail.value;
    var textInputPassword = document.getElementsByName("userPassword");
    var userPassword = textInputPassword.value;
    var textInputRepeatPassword = document.getElementsByName("repeatPassword");
    var repeatPassword = textInputRepeatPassword.value;
    if (userName === undefined || userPhone === undefined || userEmail === undefined || userPassword === undefined) {
        alert("Введите все параметры, пожалуйста!");
    }
    if (repeatPassword !== userPassword) {
        alert("Пароли не совпадают! Повторите попытку!");
    }
    else {
        alert("Поздравляем, " + userName + ", " + "регистрация прошла успешно!");
    }
}


// window.onload = addUser;

// function addUser() {
//     var buttonName = document.getElementById("addParams");
//     buttonName.onclick = handleButtonClick;
// }

// function handleButtonClick() {
//     var textInputName = document.getElementById("userName");
//     var userName = textInputName.value;
//     var textInputAge = document.getElementById("userAge");
//     var userAge = textInputAge.value;
//     if (userName == "" || userAge == "") {
//         alert("Введите параметры, пожалуйста!");
//     }
//     else {
//         alert("Ваше имя: " + userName + " Ваш возраст: " + userAge);
//     }
// }