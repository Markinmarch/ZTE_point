window.onload = addUser;

function addUser() {
    var buttonName = document.getElementById("addUser");
    buttonName.onclick = handleButtonClick;
    // buttonName.onclick = checkCorrectUserPhone;
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
        alert("Ваше имя: " + userName + " Ваш возраст: " + userPhone);
    }
}

// function checkCorrectUserPhone() {
//     var userPhone = document.getElementById("userPhone").value;
//     var checkPhone = userPhone.match(/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im);

//     if (checkPhone === false) {
//         alert("Номер телефона введён некорректно. Повторите попытку.");
//     }
// }