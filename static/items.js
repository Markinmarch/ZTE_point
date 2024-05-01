window.onload = searchItem;

function searchButton() {
    var buttonName = document.getElementById("itemSearchButton");
    buttonName.onclick = searchItem;
}

function searchItem() {
    var itemKeywords = document.getElementById("itemSearch");

    if (itemKeywords.value == "") {
        alert("Перед началом поиска введите хотя бы несколько букв.")
        return false;
    }

    var searchItemData = JSON.stringify({searchKeywords: itemKeywords.value});

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/registration", true);
    xhr.setRequestHeader('content-type', 'application/json; charset=UTF-8');
    xhr.send(searchItemData);
    xhr.onload = function() {
        // if (xhr.response == "false") {
        //     alert("Адрес почты "+ userEmail.value + " уже зарегестрирован. Используйте другой.");
        //     userEmail.value = "";
        //     return false;
        // }
        // else if (xhr.response == "few characters") {
        //     alert("Пароль должен состоять минимум из 6 знаков");
        //     userPassword.value = "";
        //     repeatPassword.value = "";
        //     return false;
        // }
        // else {
        //     alert("Поздравляем, " + userName.value + ", регистрация завершена!");
        //     window.location.replace("http://localhost:5000");
        // }
    }
}
