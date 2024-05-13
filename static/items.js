$(document).on("submit", "#itemBuy", function(event){
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "/items",
        data: {
            id: $("#itemId").val(),
            count: $("#itemCount").val()
        },
        // success: function() {
        //     alert(id)
            // window.location.reload();
        // }
    })
});

$("#itemSearch").keypress(function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        $("#itemSearchButton").click();
    }
});

window.onload = resetSearch;

function resetSearch() {
    var buttonName = document.getElementById("resetSearch");
    if (buttonName.onclick) {
        window.location.replace("http://localhost:5000/items/");
    }
}

// $(document).on('submit', '#itemSearch', function(elem) {
//     // elem.preventDefault();
//     if (elem.keyCode === 13) {
//         $("#itemSearchButton").click();
//     }
//     $.ajax({
//         type: "POST",
//         url: "/items",
//         data: {
//             keywords: $("#itemSearchInput").val()
//         },
//         success: function() {
//             window.location.reload();
//         }
//     })
// });

// document.getElementById("itemSearchButton").onclick = searchItem;

// function searchItem() {
//     var keywords = document.getElementById("itemSearchInput");
//     window.location.replace("http://localhost:5000/items/search");
//     var url = new URL(window.location.href);
//     url.searchParams.set('single', keywords);
//     window.location.href = url.href;
    // if (keywords.value == "") {
    //     return true;
    // }

    // else {
    //     window.location.href += "?хуй"
    // }
// }

window.onload = searchItem;

function searchItem() {
    var buttonName = document.getElementById("itemSearchButton");
    buttonName.onclick = getSearchItems;
}

function getSearchItems() {
    var keywords = document.getElementById("itemSearchInput");

    if (keywords.value == ""){
        alert("Введите ключевые слова, пожалуйста!");
        return false;
    }
    window.location.replace("http://localhost:5000/items/search?keywords=" + keywords.value);
    
    // var url = new URL(window.location.href);
    // url.searchParams.set('keywords', keywords.value);
    // window.location.href = url.href;

    // var xhr = new XMLHttpRequest();
    // xhr.open("POST", "/registration", true);
    // xhr.setRequestHeader('content-type', 'application/json; charset=UTF-8');
    // xhr.send(userData);
    // xhr.onload = function() {
    //     if (xhr.response == "false") {
    //         alert("Адрес почты "+ userEmail.value + " уже зарегестрирован. Используйте другой.");
    //         userEmail.value = "";
    //         return false;
    //     }
    //     else if (xhr.response == "few characters") {
    //         alert("Пароль должен состоять минимум из 6 знаков");
    //         userPassword.value = "";
    //         repeatPassword.value = "";
    //         return false;
    //     }
    //     else {
    //         alert("Поздравляем, " + userName.value + ", регистрация завершена!");
    //         window.location.replace("http://localhost:5000");
    //     }
    // }
    
}